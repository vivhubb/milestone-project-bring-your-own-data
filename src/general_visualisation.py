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