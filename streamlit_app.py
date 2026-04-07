import streamlit as st
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Function to clean ticket text
def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove extra spaces
    text = text.strip()
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

# Load the saved models
model_category = joblib.load("model/category_model.pkl")
model_priority = joblib.load("model/priority_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

# Function to predict category and priority
def predict_ticket(text):
    cleaned = clean_text(text)                 # Preprocess the ticket text
    vector = vectorizer.transform([cleaned])   # Convert to TF-IDF
    category = model_category.predict(vector)[0]
    priority = model_priority.predict(vector)[0]
    return category, priority

# Streamlit interface
st.title("Support Ticket Classifier & Prioritizer")
ticket_text = st.text_area("Enter your support ticket here:")

if st.button("Predict"):
    category, priority = predict_ticket(ticket_text)
    st.success(f"Predicted Category: {category}")
    st.success(f"Predicted Priority: {priority}")