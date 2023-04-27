import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram


def load_data(path):
    data = pd.read_csv(path)
    data['ex_showroom_price'].fillna(value=data['selling_price'], inplace=True)

    return data


def build_df():
    data = load_data('data/data.csv')

    df = pd.DataFrame(data, columns=['year', 'km_driven', 'selling_price', 'owner'])
    df['year'] = df['year'].astype(str)
    owner_count = np.array(list(map(lambda x: re.search('[0-9]*', x).group(0), df['owner'].values)))
    df['owner'] = owner_count

    return df


def visualisation_pky(df):
    fig = px.bar(df.groupby('year').mean()[['selling_price', 'km_driven']], barmode='group')

    return fig


def visualisation_po(df):
    fig = px.bar(df, x='owner', y='selling_price')

    return fig


def visualisation_pocy(df):
    dict = {}
    for i in range(len(df['owner'])):
        key = (df['owner'][i], df['year'][i])
        if key in dict:
            dict[key].append(df['selling_price'][i])
        else:
            dict[key] = [df['selling_price'][i]]

    sorted_keys = sorted(dict.keys())

    mean_selling_prices = []
    for key in sorted_keys:
        mean_selling_prices.append([key[0], key[1], sum(dict[key])/len(dict[key])])

    groups = {}
    for item in mean_selling_prices:
        owner_count = item[0]
        if owner_count in groups:
            groups[owner_count].append(item)
        else:
            groups[owner_count] = [item]

    fig = go.Figure()
    for owner_count in groups:
        dict = groups[owner_count]
        x_values = [str(item[1]) for item in dict]
        y_values = [item[2] for item in dict]
        fig.add_trace(go.Bar(x=x_values, y=y_values, name='Owner count: ' + str(owner_count)))

    return fig


def visualisation_outliers(df, x, y):
    fig = px.scatter(df, x=x, y=y)

    return fig


def calculate_price_difference(df):
    data = load_data('data/data.csv')

    df = pd.DataFrame(data, columns=['year', 'km_driven', 'selling_price', 'ex_showroom_price'])

    price_difference = df['ex_showroom_price'] - df['selling_price']
    df['price_difference'] = price_difference

    return df


def visualisation_kmpd(df):
    fig = px.line(df.groupby('km_driven').mean()[['price_difference']],
                    y='price_difference', 
                    range_x=[0, 120000], 
                    range_y=[-50000, 220000],)

    return fig

# build_correlatin_matrix & corr_matrix_heatmap code built based on
# https://github.com/faridjos/milestone-project-heritage-housing-issues/blob/main/jupyter_notebooks/HouseSalePrices.ipynb
def build_correlation_matrix():
    df = load_data('data/data.csv')
    owner_count = np.array(list(map(lambda x: re.search('[0-9]*', x).group(0), df['owner'].values)))
    df['owner'] = owner_count
    df.drop(columns=['name', 'seller_type'], inplace=True)
    lst = []
    # Remove first zeros and missing values
    for col in df.columns[df.dtypes!='object'].to_list():
        if col != 'selling_price':
            df1 = df[df[col]!=0]
            df2 = df1[df1[col].notnull()]
            df3 = df2.filter(['selling_price', col])
            corr_spearman = df3.corr(method='spearman')['selling_price'][1:].round(2)
            lst.append(corr_spearman[col])
    corr_num = pd.Series(index=df.columns[df.dtypes!='object'].drop(['selling_price']).to_list(), data=lst).sort_values(key=abs, ascending=False)

    lst = []
    for col in df.columns[df.dtypes=='object'].to_list():
        df1 = df[df[col]!='None']
        df2 = df1[df1[col].notnull()]
        df4 = df2.filter(['selling_price', col])
        corr_spearman = df4.corr(method='spearman')['selling_price'][1:].round(2)
        lst.append(corr_spearman[col])
    corr_object = pd.Series(index=df.columns[df.dtypes=='object'].to_list(), data=lst).sort_values(key=abs, ascending=False)

    corr = pd.concat([corr_num, corr_object]).sort_values(key=abs, ascending=False).round(2)
    corr_df = pd.DataFrame(index=['selling_price'], columns=corr.index, data=corr.values.reshape(1,-1).tolist())
    corr_df_rev = corr_df[corr_df.columns[::-1]]

    return corr_df_rev


def corr_matrix_heatmap(corr_df_rev):
    fig, axes = plt.subplots(figsize=(15,6))
    annot_size = 8

    # Retain only correlation values above 0.4
    mask = np.zeros_like(corr_df_rev, dtype=np.bool_)
    mask[corr_df_rev.abs() < 0.4] = True

    sns.heatmap(data=corr_df_rev, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, annot_kws={"size": annot_size}, ax=axes,
                linewidth=0.5)

    return fig


def accuracy_visualisation(y, y_pred, title):
    fig = px.scatter(x=y, y=y_pred, trendline='ols', 
                    labels={'x': 'actual price',
                            'y': 'predicted price'},
                    title=title)

    return fig
 