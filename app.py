import streamlit as st
import joblib
import numpy as np
st.title('AI News Lens (Real or Fake)')
st.write('Enter a news headline to check if it\'s real or fake.')
headline = st.text_input('News Headline')
if st.button("Predict"):
    st.success('This is a demo - add your model logic.')

