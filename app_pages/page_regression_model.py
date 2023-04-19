import streamlit as st
from src.regression_model import *


def regression_model():
    st.title('**Model Evaluation**')

    e, x, y, model = train_model()
    st.write('Train Set  \n')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    e, y_pred = test_model(model, x, y)
    st.write('Test Set')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    print(y_pred)
