import streamlit as st
from src.regression_model import *
from src.general_visualisation import accuracy_visualisation


def regression_model():
    st.title('**Model Evaluation**')

    e, x, y, y_train, y_pred, model = train_model()
    st.write('**Train Set**  \n')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    fig1 = accuracy_visualisation(y_train, y_pred, 'Train Set')

    e, y_pred = test_model(model, x, y)
    st.write('**Test Set**')
    st.write(f'R2 score: {e[0]}  \n')
    st.write(f'Mean squared error: {e[1]}  \n')
    st.write(f'Mean absolute error: {e[2]}  \n')
    st.write(f'Root mean squared error: {e[3]}  \n')

    fig2 = accuracy_visualisation(y, y_pred, 'Test Set')

    st.write('### **Predicted versus actual sale price scatterplot**')
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
