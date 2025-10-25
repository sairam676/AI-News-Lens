import streamlit as st
import pickle

# --- Page setup ---
st.set_page_config(
    page_title="AI News Lens",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("📰 AI News Lens - Fake News Detection")
st.write("Enter a news headline below to check if it's Real or Fake.")

# --- Load model and vectorizer ---
@st.cache_data
def load_model_vectorizer():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model_vectorizer()

# --- User input ---
headline = st.text_input("Enter news headline:")

# --- Prediction ---
if st.button("Predict"):
    if headline.strip() == "":
        st.warning("Please enter a headline")
    else:
        # Convert text to features
        X = vectorizer.transform([headline])
        # Make prediction (1 = Real, 0 = Fake)
        pred = model.predict(X)[0]
        result = "Real" if pred == 1 else "Fake"
        st.success(f"Prediction: {result}")
