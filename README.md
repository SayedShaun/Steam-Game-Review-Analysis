# Steam Game Review Classification

This project focuses on classifying Steam game reviews using various machine learning models to predict sentiment analysis.

## Overview

The aim of this project is to develop a classification system for Steam game reviews. The project utilizes a dataset (`steam_reviews.csv`) containing textual reviews along with corresponding sentiment labels. The models implemented in this project include:
- Decision Tree Classifier (`DecisionTreeClassifier.joblib`)
- Logistic Regression Classifier (`LogisticRegression.joblib`)
- Multinomial Naive Bayes Classifier (`MultinomialNB.joblib`)
- Random Forest Classifier (`RandomForestClassifier.joblib`)
- Support Vector Machine Classifier (`SVM.joblib`)
- XGBoost Classifier (`XGBClassifier.joblib`)

## File Structure

- **.streamlit**: Configuration for theming in the Streamlit app.
- **Images**: Images related to the project or for use within the app.
- **Models**: Contains pre-trained models and a notebook (`Notebook.ipynb`) detailing model training and evaluation.
- **app.py**: The Streamlit web application for interacting with the models and conducting predictions.
- **requirements.txt**: Necessary dependencies and packages required to run the project.
- **steam_reviews.csv**: Dataset containing Steam game reviews for training and testing.

## Usage

   ```

### Model Usage

The pre-trained models are available in the `Models` directory. To use them in your own scripts:

1. Load the desired model using a library like `joblib`.
2. Utilize the model's `predict` method to classify new Steam game reviews.

## Contribution

Contributions to enhance the models, add new features, or improve the app are welcome! Fork the repository, create a new branch, make your changes, and submit a pull request.

---
Feel free to personalize this README by adding or modifying sections based on your specific project details or additional information you want to include.
