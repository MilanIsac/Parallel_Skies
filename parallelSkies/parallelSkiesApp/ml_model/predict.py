import joblib
import pandas as pd
import os

# Load the model once when the module is imported
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'temperature_model.pkl')
model = joblib.load(MODEL_PATH)

def predict_temperature(lat, lon, month, day, hour):
    X_input = pd.DataFrame([{
        'latitude': lat,
        'longitude': lon,
        'month': month,
        'day': day,
        'hour': hour
    }])
    kelvin = model.predict(X_input)[0]
    return round(kelvin - 273.15, 2)  # return °C
