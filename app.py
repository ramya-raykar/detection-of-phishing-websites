import streamlit as st
import joblib

# Load the trained model
model = joblib.load("phishing_model.joblib")

# Title
st.title("🔍 Phishing Website Detection")

# User input
url = st.text_input("Enter a website URL")

# Predict button
if st.button("Predict"):
    if url:
        try:
            result = model.predict([url])

            # Display result
            if result[0] == 1:
                st.error("⚠ Phishing Website Detected!")
            else:
                st.success("✅ Legitimate Website")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.warning("Please enter a URL to continue.")
