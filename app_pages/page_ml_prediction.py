import streamlit as st
from src.ML_prediction import *

def ml_prediction():
    df = load_validation_df()

    st.write('**Validation dataframe**')
    st.dataframe(df)