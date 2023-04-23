import streamlit as st
import altair
from src.general_visualisation import *


def statistics_visualisation():
    df = build_df()

    st.write('## Visualisations')

    st.write('#### Correlation Matrix')
    st.write(corr_matrix_heatmap())

    st.write('#### Dataframe used for below visualisations')
    st.dataframe(df)

    st.write('#### Selling price and KM driven per year')
    st.plotly_chart(visualisation_pky(df))

    st.write('#### Selling price by owner count')
    st.plotly_chart(visualisation_po(df))

    st.write('#### Selling Price by Owner Count and Year')
    st.plotly_chart(visualisation_pocy(df))

    st.write('#### Identifying outliers')
    st.write('* **Selling Price by Year**')
    st.plotly_chart(visualisation_outliers(df, x='year', y='selling_price'))
    st.write('* **Selling Price by KMs driven**')
    st.plotly_chart(visualisation_outliers(df, x='km_driven', y='selling_price'))


    st.write('#### **Dataframe used for below visualisation**')
    df = calculate_price_difference(df)
    st.dataframe(df)

    st.write('#### **How KMs driven affect price drop**')
    st.plotly_chart(visualisation_kmpd(df))
