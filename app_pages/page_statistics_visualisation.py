import streamlit as st
import altair
from src.general_visualisation import *


def statistics_visualisation():
    df = build_df()

    st.write('**Dataframe used for below visualisation**')
    st.dataframe(df)

    st.write('**Selling price and KM driven per year**')
    st.bar_chart(visualisation_pky(df))

    st.write('**Selling price by owner count**')
    st.pyplot(visualisation_po(df))

    st.write('**Selling Price by Owner Count and Year**')
    st.pyplot(visualisation_pocy(df))

    st.write('**Identifying outliers**')
    st.plotly_chart(visualisation_outliers(df))
