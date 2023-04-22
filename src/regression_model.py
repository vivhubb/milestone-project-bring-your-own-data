import os
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from src.general_visualisation import load_data
from src.data_management import drop_outliers, load_data, save_model


def train_model():
    if 'output' not in os.listdir('data/'):
        x_train = load_data('data/input/x_train.csv')
        y_train = load_data('data/input/y_train.csv')
        y_train = y_train.squeeze()

        models = {
            'Linear Regression': LinearRegression(),
            'Decision Tree Regression': DecisionTreeRegressor(),	
            'Random Forest Regression': RandomForestRegressor(),	
            'Gradient Boosting Regression': GradientBoostingRegressor(),	
            'Support Vector Regression': SVR()
        }

        model_obj = {}
        for name, model in models.items():
            scores = cross_val_score(model, x_train, y_train, cv=5, scoring='r2')
            r2_scores = np.mean(scores)
            model_obj[model] = r2_scores

        # get the best model
        model = sorted(model_obj, key=model_obj.get, reverse=True)[0]
        model.fit(x_train, y_train)
        save_model(model, 'data/output/model.pkl')

        model.fit(x_train.drop(columns=['owner', 'ex_showroom_price']), y_train)
        save_model(model, 'data/output/best_model.pkl')
    
def test_model(model):
    x_test = load_data('data/input/x_test.csv')
    y_test = load_data('data/input/y_test.csv')
    y_test = y_test.squeeze()

    y_pred = model.predict(x_test)

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