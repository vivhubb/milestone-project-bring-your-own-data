import streamlit as st
from src.data_management import split_data
from src.regression_model import train_model


def project_summary():
    split_data()
    train_model()
    
    st.title('Quick Project Summary')
    st.info(
        f"* **General information**  \n"
        f"* **Project Dataset**  \n"
    )
    st.write(
        f"* For more information, you can visit the "
        f"[Project README file](https://github.com/vivhubb/milestone-project-bring-your-own-data/blob/main/README.md)"
    )
    st.warning(
        f"The project has X business requirements:  \n"
        f"* 1 -  \n"
        f"* 2 -  \n"
        )
