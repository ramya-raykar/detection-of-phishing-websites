import streamlit as st
import joblib

# Load the trained model
model = joblib.load('phishing_model.joblib')

# Title
st.title("Phishing Website Detection")

# User input
url = st.text_input("Enter a website URL")

# Predict button
if st.button("Predict"):
    # Replace this with your actual feature extraction function
    features = extract_features(url)  # Your custom logic
    features = [str(f) if f is not None else "" for f in features]
    result = model.predict([features])

    # Display result
    if result[0] == 1:
        st.error("⚠ Phishing Website Detected!")
    else:
        st.success("✅ Legitimate Website")
def extract_features(url):
    features = []
    features.append(len(url))                   # Length of URL
    features.append(int('https' not in url))    # HTTPS check
    features.append(int('.com' not in url))     # .com presence
    # Add more features based on how your model was trained
    return features
