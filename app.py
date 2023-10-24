from flask import Flask, render_template, request, app, jsonify, url_for
import joblib

import pandas as pd
import numpy as np

app = Flask(__name__)
model = joblib.load('linear_regression.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    input_data = np.array(list(data.values())).reshape(1,-1)
    print(input_data)
    prediction = model.predict(input_data)
    return jsonify(prediction[0])

@app.route('/predict', methods=['POST'])
def predict():
    # data = [float(x) for x in request.form.values()]
    tv = float(request.form.get('TV'))
    radio = float(request.form.get('Radio'))
    newspaper = float(request.form.get('Newspaper'))

    # Create a DataFrame with the input data
    input_df = pd.DataFrame([[tv, radio, newspaper]])
    # input_data = np.array(data)
    prediction = model.predict(input_df)[0]
    return render_template('home.html', prediction = f'The result is {prediction}')


if __name__ == '__main__':
    app.run(debug=True)