(np.round(prediction[0], 2))
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open('Car.pkl', 'rb'))
car_data = pd.read_csv('cleaned_car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    car_companies = sorted(car_data['company'].unique())
    car_models = sorted(car_data['name'].unique())
    manufacturing_years = sorted(car_data['year'].unique(), reverse=True)
    fuel_types = car_data['fuel_type'].unique()

    return render_template('index.html', car_companies=car_companies, car_models=car_models,
                           manufacturing_years=manufacturing_years, fuel_types=fuel_types)

@app.route('/predict', methods=["POST"])
@cross_origin()
def predict():
    selected_company = request.form.get('selected_company')
    selected_car_model = request.form.get('selected_car_model')
    manufacturing_year = request.form.get('manufacturing_year')
    selected_fuel_type = request.form.get('selected_fuel_type')
    kilometers_driven = request.form.get('kilometers_driven')

    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                            data=np.array([selected_car_model, selected_company, manufacturing_year,
                                                           kilometers_driven, selected_fuel_type]).reshape(1, 5)))

    return str(np.round(prediction[0], 2))


if __name__ == '__main__':
    app.run(debug=True)

