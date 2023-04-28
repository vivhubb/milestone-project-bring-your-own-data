import streamlit as st


def hypothesis_and_validation():
    st.write('#### Project Hypothesis and Validation')
    st.success(
        '''
        * We initially suspected that the 2 most important features would be the **year** and the **Kms driven**.  \n
        * The correlation study showed that another important feature is the **ex showroom price**. 
        * Based on these result we decided to do the price prediction based on these **3 most important features**.
        '''
    )