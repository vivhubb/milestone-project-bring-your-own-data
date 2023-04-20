import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.general_visualisation import load_data
from src.data_management import drop_outliers, load_data


def train_model():
    x_train = load_data('data/input/x_train.csv')
    y_train = load_data('data/input/y_train.csv')
    y_train = y_train.squeeze()
    
    x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x_train)

    model = LinearRegression()
    model.fit(x_, y_train)

    y_pred = model.predict(x_)
    e = calculate_errors(y_train, y_pred)

    return e, y_train, y_pred, model

    
def test_model(model):
    x_test = load_data('data/input/x_test.csv')
    y_test = load_data('data/input/y_test.csv')
    y_test = y_test.squeeze()

    x_ = PolynomialFeatures(degree=2, include_bias=True).fit_transform(x_test)
    
    y_pred = model.predict(x_)
    e_test = calculate_errors(y_test, y_pred)

    return e_test, y_test, y_pred


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