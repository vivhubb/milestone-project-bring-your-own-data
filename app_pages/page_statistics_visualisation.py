import streamlit as st
import altair
from src.general_visualisation import *


def statistics_visualisation():
    df = build_df()

    st.write('**Dataframe used for below visualisation**')
    st.dataframe(df)

    st.write('**Selling price and KM driven per year**')
    st.bar_chart(visualisation_pky(df))
