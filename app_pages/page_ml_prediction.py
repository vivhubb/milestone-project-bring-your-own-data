import pandas as pd
import streamlit as st
from src.data_management import get_date, save_data
from src.ML_prediction import predict_price, predict_from_csv

def ml_prediction():
    st.write('## Predict Sale Price')

    st.warning(
        '''
        The **Price Predictor** can be used to predict price for 
        1 motorcycle at a time. Fill out below with the correct details 
        and click **"Predict Price"** to see the result.
        '''
        )

    with st.form(key='form'):
        year_input = st.number_input(label='**year**', min_value=1885, max_value=int(get_date()), value=2002)
        km_input = st.number_input(label='**KMs driven**', min_value=0, value=22000)
        ex_showroom_price_input = st.number_input(label='**ex showroom price**', min_value=00, value=44000)
        submit = st.form_submit_button(label='**Predict Price**')

    if submit:
        price = int(predict_price([[year_input, km_input, ex_showroom_price_input],])[0])
        st.write(f'**Predicted Price:** {price}')


    st.warning(
        '''
        If you wish to perform prediction for a series of motorcylces, 
        you can do so in 2 step. First you download the CSV input template
        and fill it out with the bikes' details you would like to predict 
        prices for. Secondly, using the "Browse files" button you can 
        upload the CSV file for prediction.
        '''
    )

    st.write('1 - Download input template :')
    with open('template/template.csv', 'rb') as f:
        st.download_button('**Download CSV template**', f, file_name='template.csv')

    upload = st.file_uploader(label='2 - **Upload CSV file :**')

    if upload is not None:
        save_data('uploads/input.csv', pd.read_csv(upload))

        data = predict_from_csv()

        st.write('**Predicted Prices :**')
        st.write(data)
