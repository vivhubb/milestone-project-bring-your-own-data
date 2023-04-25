import streamlit as st
from src.regression_model import *
from src.general_visualisation import accuracy_visualisation
from src.data_management import load_model, load_data
from src.regression_model import calculate_errors


def regression_model():
    st.info('* We have agreed with the client on an R2 score of at least 0.75')

    st.write('#### Model Evaluation')

    model = load_model('data/output/model.pkl')
    x = load_data('data/input/x_train.csv')
    y = load_data('data/input/y_train.csv')
    y = y.squeeze()

    y_pred = model.predict(x)
    e = calculate_errors(y, y_pred)

    st.write('* **Train Set**  \n')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    fig1 = accuracy_visualisation(y, y_pred, 'Train Set')

    e, y, y_pred = test_model(model)
    st.write('* **Test Set**')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    fig2 = accuracy_visualisation(y, y_pred, 'Test Set')

    st.write('#### Actual vs Predicted selling price scatterplot')
    st.write(fig1)
    st.write(fig2)
