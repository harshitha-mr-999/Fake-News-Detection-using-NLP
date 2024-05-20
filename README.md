

# Fake News Detection Using NLP

This project implements a fake news detection system using Natural Language Processing (NLP) techniques. It includes a Streamlit web application that allows users to input news articles and receive predictions on whether they are reliable or unreliable.

## Project Structure

The project directory contains the following files and directories:

- `app.py`: Streamlit web application code for fake news detection.
- `Fake_news_detection_using_NLP.ipynb`: Jupyter Notebook containing the code for model training and evaluation.
- `vector.pkl`: Pickled file containing the trained TF-IDF vectorizer.
- `model.pkl`: Pickled file containing the trained classification model.
- `templates/`: Directory containing HTML templates for the Streamlit app.
- `static/`: Directory containing static assets for the Streamlit app, such as CSS files.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fake-news-detection.git

2.Install the required dependencies:
pip install -r requirements.txt

3.Run the Streamlit app:
streamlit run app.py

Usage
Input a news article into the text area provided.
Click the "Predict" button to receive a prediction on whether the article is reliable or unreliable.
The prediction will be displayed as a success (reliable) or warning (unreliable) message

Model Training
The model used for fake news detection was trained using a Jupyter Notebook (Fake_news_detection_using_NLP.ipynb). It includes preprocessing steps, feature extraction using TF-IDF vectorization, and training of a classification model.

