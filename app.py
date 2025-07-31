import streamlit as st
import pickle

# Load model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

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