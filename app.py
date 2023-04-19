import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_project_summary import project_summary
from app_pages.page_statistics_visualisation import statistics_visualisation
from app_pages.page_ml_prediction import ml_prediction
from app_pages.page_regression_model import regression_model

app = MultiPage(app_name='Price Predictor')

app.add_page('Quick Project Summary', project_summary)
app.add_page('Visualisation', statistics_visualisation)
app.add_page('Predict Selling Price', ml_prediction)
app.add_page('ML Regression Model', regression_model)

app.run()
