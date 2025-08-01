import streamlit as st
import joblib
import re

# Load model
model = joblib.load("phishing_model.joblib")

# --- Your feature extraction function ---
def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(url.count('.'))
    features.append(1 if url.startswith("https") else 0)
    # Add any other features you used during training
    return features

# Streamlit UI
st.title("🔍 Phishing Website Detection")
url = st.text_input("Enter a website URL")

if st.button("Predict"):
    if url:
        try:
            features = extract_features(url)
            result = model.predict([features])

            if result[0] == 1:
                st.error("⚠ Phishing Website Detected!")
            else:
                st.success("✅ Legitimate Website")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a URL to continue.")
