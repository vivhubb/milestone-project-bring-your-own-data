import pandas as pd
import streamlit as st
from src.data_management import get_date, save_data
from src.ML_prediction import predict_price, predict_from_csv

def ml_prediction():
    st.write('## Predict Sale Price')

    with st.form(key='form'):
        year_input = st.number_input(label='year', min_value=1885, max_value=int(get_date()), value=2002)
        km_input = st.number_input(label='KMs driven', min_value=0, value=22000)
        submit = st.form_submit_button(label='**Predict Price**')

    if submit:
        price = int(predict_price([[year_input, km_input],])[0])
        st.write(f'**Predicted Price:** {price}')

    st.write('**Download input template :**')
    with open('template/template.csv', 'rb') as f:
        st.download_button('**Download CSV template**', f, file_name='template.csv')

    upload = st.file_uploader(label='**Upload CSV file for Price Prediction :**')

    if upload is not None:
        save_data('uploads/input.csv', pd.read_csv(upload))

        data = predict_from_csv()

        st.write('**Predicted Prices :**')
        st.write(data)

