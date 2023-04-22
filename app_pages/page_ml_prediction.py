import streamlit as st
from src.data_management import get_date
from src.ML_prediction import predict_price

def ml_prediction():
    st.write('#### **Predict Sale Price**')

    with st.form(key='form'):
        year_input = st.number_input(label='year', min_value=1885, max_value=int(get_date()), value=2002)
        km_input = st.number_input(label='KMs driven', min_value=0, value=22000)
        submit = st.form_submit_button(label='Predict Price')

    if submit:
        price = int(predict_price([[year_input, km_input],])[0])
        st.write(f'**Predicted Price:** {price}')

