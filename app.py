import streamlit as st
from app_pages.multipage import MultiPage

def page_summary():
    st.info('string')

app = MultiPage(app_name='Price Predictor')

app.add_page('Quick Project Summary', page_summary)

app.run()
