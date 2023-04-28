import streamlit as st
import altair
from src.general_visualisation import *


def statistics_visualisation():
    df = build_df()

    st.write('## Motorcycles Price Study')

    # general overview
    st.warning(
        '''
        * The client is interested in understanding the patterns of 
        the motorbikes dataset so that the client can learn the most 
        relevant variables correlated to price changes.
        '''
        )

    # title
    st.write('## Visualisations')

    # correlation matrix
    st.warning(
        '''
        * A correlation study was conducted to find the most 
        important variables for determining a motorcycle's sale price.
        '''
        )
    if st.checkbox('**Correlation Matrix**'):
        corr_df_rev = build_correlation_matrix()
        st.write(corr_matrix_heatmap(corr_df_rev))

        st.warning(
            '''
            A **correlation matrix** is a table that displays the 
            pairwise correlation coefficients between a set of variables. 
            In other words, it shows how strongly each variable is related 
            to every other variable in the set.
            '''
        )
        st.info(
            f"**Variables explained** (sorted by level of importance)**:**  \n"
            f"The 3 most important variables are:  \n"
            f"* **year:** shows the year of manufacturing  \n"
            f"* **km_driven:** shows the mileage for the motorcycle  \n"
            f"* **ex_showroom_price:** shows the initial price of the motorbike  \n\n"
            f"The other variables:  \n"
            f"* **owner:** counts how many owners the bike had previously  \n"
            f"* **name**: holds information about the brand and model of the bikes  \n"
            f"* **seller_type**: categorical variable showing if the seller is an individual or a dealer  \n"
        )

    st.write('**Dataframe used for below visualisations**')
    st.write(
        f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns"
        )
    st.dataframe(df)

    if st.checkbox('**Selling price and KM driven per year**'):
        st.plotly_chart(visualisation_pky(df))

    if st.checkbox('**Selling price by owner count**'):
        st.plotly_chart(visualisation_po(df))

    if st.checkbox('**Selling Price by Owner Count and Year**'):
        st.plotly_chart(visualisation_pocy(df))

    if st.checkbox('**Identifying outliers**'):
        st.write('* **Selling Price by Year**')
        st.plotly_chart(visualisation_outliers(
            df, x='year', y='selling_price'))
        st.write('* **Selling Price by KMs driven**')
        st.plotly_chart(visualisation_outliers(
            df, x='km_driven', y='selling_price'))

    st.write('**Dataframe used for below visualisation**')
    df = calculate_price_difference(df)
    st.write(
        f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns"
        )
    st.dataframe(df)

    if st.checkbox('**How KMs driven affect price drop**'):
        st.plotly_chart(visualisation_kmpd(df))
