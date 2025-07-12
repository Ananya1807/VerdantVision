import requests
import pickle
import pandas as pd

# Blynk credentials
BLYNK_TOKEN = "s8eeiG-XJSLDomSTpr0vd8IX0jqxnO-q"
BASE_URL = f"https://blynk.cloud/external/api"

# Load model
with open('model/watering_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Step 1: Get data from Blynk
def get_sensor_data():
    temp = float(requests.get(f"{BASE_URL}/get?token={BLYNK_TOKEN}&pin=V0").text)
    humidity = float(requests.get(f"{BASE_URL}/get?token={BLYNK_TOKEN}&pin=V1").text)
    moisture = float(requests.get(f"{BASE_URL}/get?token={BLYNK_TOKEN}&pin=V2").text)
    return temp, humidity, moisture

# Step 2: Preprocess and predict
def make_decision(temp, humidity, moisture):
    df = pd.DataFrame([[temp, humidity, moisture]], columns=['MaxT', 'Humidity', 'Moisture'])
    # Add dummy values for MinT, WindSpeed, Precipitation if needed
    df['MinT'] = temp - 5
    df['WindSpeed'] = 2
    df['Precipitation'] = 0
    X = df[['MaxT', 'MinT', 'WindSpeed', 'Humidity', 'Precipitation']]
    # Preprocess with StandardScaler if used
    pred = model.predict(X)[0]
    return pred

# Step 3: Send command to ESP32 via Blynk
def send_to_blynk(prediction):
    msg = "PUMP IS ON" if prediction == 1 else "PUMP IS OFF"
    requests.get(f"{BASE_URL}/update?token={BLYNK_TOKEN}&pin=V3&value={msg}")
    print("Decision sent to Blynk:", msg)

# Run everything
t, h, m = get_sensor_data()
decision = make_decision(t, h, m)
send_to_blynk(decision)
