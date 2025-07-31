
import streamlit as st
import pickle

# Load model
import joblib
model = joblib.load('phishing_model.joblib')

st.title("Phishing Website Detection")
url = st.text_input("Enter website URL features")

if st.button("Predict"):
    # You must replace this with your real feature extraction!
    # Right now it's dummy input
    features = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]  # <-- dummy features
    result = model.predict(features)
    if result[0] == 1:
        st.error("⚠ Phishing Website Detected!")
    else:
        st.success("✅ Legitimate Website")
# Before prediction
features = extract_features(user_input)  # or however you're generating features
features = [str(f) if f is not None else "" for f in features]
result = model.predict(features)
