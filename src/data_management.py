import os
import re
import joblib
import numpy as np
import pandas as pd
from datetime import date
from sklearn.model_selection import train_test_split


def load_dataset(path):
    data = pd.read_csv(path)
    data['ex_showroom_price'].fillna(value=data['selling_price'], inplace=True)

    return data


def load_data(path):
    data = pd.read_csv(path)

    return data


def save_data(path, data):
    data.to_csv(path, index=False)


def drop_outliers(df, df_col):
    q1, q3 = np.percentile(df[df_col], [25, 75])

    # interquartile range
    IQR = q3 - q1
    # upper limit
    ul = q3+1.5*IQR
    # lower limit
    ll = q1-1.5*IQR

    return df[(df[df_col] >= ll) & (df[df_col] <= ul)]


def split_data():
    if 'input' not in os.listdir('data'):
        df = load_dataset('data/data.csv')

        owner_count = np.array(list(map(lambda x: re.search('[0-9]*', x).group(0), df['owner'].values)))
        df['owner'] = owner_count
        df.drop(['name', 'seller_type'], axis=1, inplace=True)

        df = drop_outliers(df, 'selling_price')
        df = drop_outliers(df, 'km_driven')

        y = df['selling_price']

        x_train, x_test, y_train, y_test = train_test_split(df.drop(['selling_price'], axis=1), y, test_size=.2, random_state=1)

        os.mkdir('data/input/')
        save_data('data/input/x_train.csv', x_train)
        save_data('data/input/x_test.csv', x_test)
        save_data('data/input/y_train.csv', y_train)
        save_data('data/input/y_test.csv', y_test)


def get_date():
    return date.today().strftime('%Y')


def save_model(model, filename):
    if not os.path.isdir(os.path.dirname(filename)):
        os.mkdir(os.path.dirname(filename))

    joblib.dump(model, filename)


def load_model(filename):
    return joblib.load(filename)
