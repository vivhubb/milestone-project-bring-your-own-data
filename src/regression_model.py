import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.general_visualisation import load_data


def drop_outliers(df, df_col):
    q1, q3 = np.percentile(df[df_col], [25, 75])

    IQR = q3 - q1
    ul = q3+1.5*IQR
    ll = q1-1.5*IQR

    return df[(df[df_col] >= ll) & (df[df_col] <= ul)]


def train_model():
    df = load_data('data/data.csv')

    df = drop_outliers(df, 'selling_price')
    df = drop_outliers(df, 'km_driven')

    x = df[['year', 'km_driven']]
    y = df['selling_price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.2, random_state=1)

    x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x_train)

    model = LinearRegression()
    model.fit(x_, y_train)

    y_pred = model.predict(x_)
    e = calculate_errors(y_train, y_pred)

    return e, x_test, y_test, model

    
def test_model(model, x, y):   

    x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x)
    
    y_pred = model.predict(x_)
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