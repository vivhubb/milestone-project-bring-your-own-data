import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from src.data_management import split_train_validation_test_data
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


def load_train_df():
    data = pd.read_csv('data/train/train.csv')
    df_train = pd.DataFrame(data)

    return df_train


def load_test_df():
    data = pd.read_csv('data/test/test.csv')
    df_test = pd.DataFrame(data)

    return df_test


def train_model():
    split_train_validation_test_data('data/', 0.8, 0.1, 0.1)

    df = load_train_df()
    df = df[(df['year']>=2000) & (df['km_driven']<75000)]

    x = df[['year', 'km_driven']]
    y = df['selling_price']

    # x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x)

    model = LinearRegression()
    model.fit(x, y)

    y_pred = model.predict(x)
    e = calculate_errors(y, y_pred)

    return e, model

    
def test_model(model):
    df = load_test_df()
    x = df[['year', 'km_driven']]
    y = df['selling_price']

    y_pred = model.predict(x)
    e_test = calculate_errors(y, y_pred)

    return e_test, y_pred


def calculate_errors(y, y_pred):
    # calculate R2
    r2 = r2_score(y, y_pred)

    # calculate MSE
    mse = mean_squared_error(y, y_pred)

    # calculate MAE
    mae = mean_absolute_error(y, y_pred)

    # calculate RMSE
    rmse = np.sqrt(mse)

    return [r2, mse, mae, rmse]