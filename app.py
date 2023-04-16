import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_project_summary import project_summary

app = MultiPage(app_name='Price Predictor')

app.add_page('Quick Project Summary', project_summary)

app.run()
