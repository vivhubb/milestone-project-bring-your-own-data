import streamlit as st
from src.data_management import get_date

def ml_prediction():
    st.write('#### **Predict Sale Price**')
    st.number_input(label='year', min_value=1885, max_value=int(get_date()), value=2002)
    st.number_input(label='KMs driven', min_value=0, value=22000)
    st.button(label='Predict Price')