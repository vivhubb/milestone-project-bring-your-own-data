import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import re


def load_data(path):
    data = pd.read_csv(path)
    data = data.dropna()
    data.reset_index(inplace=True)

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


def visualisation_outliers(df):
    fig = px.scatter(df, x='year', y='selling_price')

    return fig