import streamlit as st
import joblib

# Load trained pipeline
model = joblib.load("phishing_model.joblib")

st.title("🔍 Phishing Website Detection")
url = st.text_input("Enter a website URL")

if st.button("Predict"):
    if url:
        try:
            result = model.predict([url])

            if result[0] == 'bad':
                st.error("⚠ Phishing Website Detected!")
            else:
                st.success("✅ Legitimate Website")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter a URL to continue.")
