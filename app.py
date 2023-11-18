import streamlit as st
import re
import xgboost
import nltk
from nltk.stem.porter import PorterStemmer
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from PIL import  Image

image = Image.open("Images/Steam_icon_logo.png")
st.set_page_config(page_title='Steam',page_icon=image)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Steam Game Review Analysis")
input_data = st.text_area("Leave Steam Review", height=150)
def preprocess(text):
    stopwords = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from',
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're',
             's', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']
    
    cleaned_text = re.sub(r"http\S+", "", text)
    cleaned_text = re.sub(r"<[^>]*>", "", cleaned_text)
    cleaned_text = re.sub(r"[^\w\s]", "", cleaned_text)
    cleaned_text = re.sub(r"(.)\1{2,}", r"\1", cleaned_text)
    cleaned_text = re.sub(r"\d", "", cleaned_text)
    cleaned_text = " ".join([word for word in cleaned_text.split() if word.lower() not in stopwords])

    ps = PorterStemmer()
    stemmed_words = [ps.stem(word) for word in cleaned_text.split()]
    cleaned_text = " ".join(stemmed_words)
    return cleaned_text
    
def text_transform(text):
    tfidf = joblib.load("Models/tfidf")
    vector = tfidf.transform([preprocess(text)])
    return vector

def prediction(text):
    xgb = joblib.load("Models/XGBClassifier.joblib")
    lr = joblib.load("Models/LogisticRegression.joblib")
    mnb = joblib.load("Models/MultinomialNB.joblib")
    dt = joblib.load("Models/DecisionTreeClassifier.joblib")
    svm = joblib.load("Models/SVM.joblib")

    naive_bayes = mnb.predict(text)
    support_vector = svm.predict(text)
    xgboost_model = xgb.predict(text)
    decision_tree = dt.predict(text)
    logistic_regression = lr.predict(text)
    
    predictions = [naive_bayes, support_vector, xgboost_model, decision_tree, logistic_regression]
    predictions_array = np.array(predictions)
    majority_predictions = np.round(np.mean(predictions_array, axis=0)).astype(int)
    return majority_predictions

if st.button("Predict", use_container_width=True):
    if len(input_data.strip()) == 0:
        st.header("Please Provide Text")
    else:
        vector = text_transform(input_data)
        output = prediction(vector)
        if output == 0:
            st.image("Images/Not Recommended.gif")
        elif output == 1:
            st.image("Images/Recommended.gif")
