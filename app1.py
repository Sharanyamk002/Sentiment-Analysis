import streamlit as st
import joblib

model = joblib.load('sentiment-model.pkl')
sentiment_labels = {'1': 'Positive', '0': 'Negative'}

st.title("Sentiment Analysis")
user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    predicted_sentiment = model.predict([user_input])[0]
    print("Predicted sentiment value:", predicted_sentiment)
    predicted_sentiment_label = sentiment_labels.get(str(predicted_sentiment), "Unknown")
    print("Predicted sentiment label:", predicted_sentiment_label)
    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")
