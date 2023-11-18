![steam analysis demp](https://github.com/SayedShaun/Steam-Review-Analysis/assets/126845316/66e2f474-247d-49c1-890f-b0e070ad61f8)

Live Demo: https://steam-review-analysis.streamlit.app
# Steam Review Analysis

## Overview

This project involves creating a Steam game review analysis system. It will take user-provided game reviews and classify whether the game is recommended or not based on the sentiment or content of the review. Essentially, it aims to assess whether a particular game is positively or negatively reviewed by users.

## Features

- **Streamlit**: Used for theming and creating an interactive interface for the analysis.
- **Data**: The 'data' directory contains the 'steam_reviews.zip' file containing the dataset.
- **Images**: Directory for storing images used in the analysis or documentation.
- **Models**: Contains trained models for the following classifiers:
  - DecisionTreeClassifier
  - LogisticRegression
  - MultinomialNB
  - SVM
  - XGBClassifier
- **Notebook.ipynb**: Jupyter notebook file containing the code for data exploration, model training, and evaluation.
- **app.py**: Python file for the Streamlit web application.
- **requirements.txt**: File listing all Python dependencies needed to run the code.

## Usage

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/steam-review-analysis.git
    cd steam-review-analysis
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit App**:

    ```bash
    streamlit run app.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust or add any additional sections, descriptions, or badges to better suit your repository. This README serves as a starting point, providing essential information for users and contributors.
