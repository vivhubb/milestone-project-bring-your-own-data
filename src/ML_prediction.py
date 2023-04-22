import numpy as np
import pandas as pd
from src.data_management import load_model, load_data


def predict_price(data):
    model = load_model('data/output/best_model.pkl')
    data = pd.DataFrame(np.array(data), columns=['year', 'km_driven'])

    return model.predict(data)


def predict_from_csv():
    data = pd.read_csv('uploads/input.csv')
    model = load_model('data/output/best_model.pkl')

    pred_price = model.predict(data.drop(columns=['name']))

    data['year'] = data['year'].astype(str)
    data['predicted price'] = pred_price.astype(int)

    return  data