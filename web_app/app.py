import os
print("------------------------------------------------")
print("PYTHON IS RUNNING FROM:", os.getcwd())
print("DOES TEMPLATES EXIST here?:", os.path.exists('templates'))
if os.path.exists('templates'):
    print("FILES INSIDE TEMPLATES:", os.listdir('templates'))
print("------------------------------------------------")

from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

model_path = os.path.join('models', 'house_model.pkl')

with open(model_path, 'rb') as file:
    model_data = pickle.load(file)

w_final = model_data['w']
b_final = model_data['b']
mu = model_data['mu']
sigma = model_data['sigma']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        stories = float(request.form['stories'])
        parking = float(request.form['parking'])

        x_raw = np.array([area, bedrooms, bathrooms, stories, parking])
        x_norm = (x_raw - mu) / sigma
        price_prediction = np.dot(x_norm, w_final) + b_final

        return render_template('index.html',
                               prediction_text=f"Estimated Price: ${price_prediction*1000:,.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")
    
if __name__ == "__main__":
    app.run(debug=True)
