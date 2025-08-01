import streamlit as st
import joblib

# Load the trained model
model = joblib.load('phishing_model.joblib')

# Title
st.title("🔍 Phishing Website Detection")

# Input URL
url = st.text_input("Enter a website URL")

# Feature extraction function
def extract_features(url):
    features = []
    features.append(len(url))                         # Length of URL
    features.append(int('https' not in url))          # No HTTPS
    features.append(int('.com' not in url))           # Missing .com
    features.append(int('@' in url))                  # Suspicious character
    features.append(int(url.count('.') > 3))          # Too many dots
    features.append(int('-' in url))                  # Hyphen usage
    features.append(int(url.startswith('http://')))   # Insecure protocol
    features.append(int(url.endswith('.zip')))        # Suspicious file type
    features.append(int('login' in url.lower()))      # Phishing keyword
    features.append(int('ip' in url.lower()))         # IP address usage
    return features

# Predict button
if st.button("Predict"):
    if url:
        features = extract_features(url)
        result = model.predict([features])

        # Display result
        if result[0] == 1:
            st.error("⚠ Phishing Website Detected!")
        else:
            st.success("✅ Legitimate Website")
    else:
        st.warning("Please enter a URL to continue.")
