import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Initialize the stemmer
port_stem = PorterStemmer()

# Load the vectorizer and model
vectorizer = pickle.load(open('vector.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Function to preprocess and stem the input content
def stemming(content):
    content = re.sub('[^a-zA-Z]', ' ', content)
    content = content.lower()
    content = content.split()
    content = [port_stem.stem(word) for word in content if word not in stopwords.words('english')]
    content = ' '.join(content)
    return content

# Function to predict if the news is fake or real
def fake_news(news):
    news = stemming(news)
    input_data = [news]
    vectorized_input = vectorizer.transform(input_data)
    prediction = model.predict(vectorized_input)
    return prediction

# Streamlit app interface
if __name__ == '__main__':
    st.title('Fake News Classification App')
    st.subheader("Input the News Content Below")
    
    # Text area for user input
    news_content = st.text_area("Enter your news content here", "", height=200)
    
    # Button to trigger prediction
    predict_button = st.button("Predict")
    
    if predict_button:
        prediction = fake_news(news_content)
        if prediction == [0]:
            st.success('Reliable')
        elif prediction == [1]:
            st.warning('Unreliable')
