import streamlit as st
from src.ML_prediction import *

def ml_prediction():
    df = load_train_df()

    st.write('**Dataframe used for training ML model**')
    st.dataframe(df)