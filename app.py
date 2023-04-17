import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_project_summary import project_summary
from app_pages.page_statistics_visualisation import statistics_visualisation

app = MultiPage(app_name='Price Predictor')

app.add_page('Quick Project Summary', project_summary)
app.add_page('Visualisation', statistics_visualisation)

app.run()
