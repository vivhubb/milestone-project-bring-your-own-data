import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    return df.groupby('year').mean()[['selling_price', 'km_driven']]


def visualisation_po(df):
    fig = plt.figure()
    plt.bar(df['owner'], df['selling_price'])
    plt.title('Selling price by owner count')
    plt.xlabel('OWNER')
    plt.ylabel('PRICE VALUE')

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

    fig = plt.figure(figsize=(11,8))

    for owner_count in groups:
        dict = groups[owner_count]
        x_values = [str(item[1]) for item in dict]
        y_values = [item[2] for item in dict]
        plt.barh(x_values, y_values, label='Owner count: ' + str(owner_count))

    plt.ylabel('YEAR')
    plt.xlabel('PRICE VALUE')
    plt.title('Selling Price by Owner Count and Year')

    plt.legend()
    return fig