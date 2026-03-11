import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Fake News Detector")
st.write("Enter a news article to check if it is Real or Fake")

# User input
news = st.text_area("Enter news text")

if st.button("Predict"):

    if news.strip() == "":
        st.warning("Please enter some text")

    else:
        news_vector = vectorizer.transform([news])
        prediction = model.predict(news_vector)[0]
        probability = model.predict_proba(news_vector).max()

        if prediction == 0:
            st.error("Prediction: FAKE")
        else:
            st.success("Prediction: REAL")

        st.write("Confidence:", round(probability, 3))