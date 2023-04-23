import streamlit as st
from src.data_management import split_data
from src.regression_model import train_model


def project_summary():
    split_data()
    train_model()

    st.write('## Quick Project Summary')
    st.info(
        f"* **General information**  \n"
        f"This dataset contains information about 1061 used motorcycles.  \n\n"

        f"* **Project Dataset**  \n"
        f"The dataset has 7 features that could potentially affect their prices. \n"
        f"The features are the following: name, selling price, year, seller type, owner, km driven, ex showroom price."
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
