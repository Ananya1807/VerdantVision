# 🌿 Verdant Vision – AIoT-Based Smart Gardening System

**Verdant Vision** is an intelligent gardening ecosystem built using IoT, AI/ML, and automation. It integrates real-time sensor data with machine learning to automate watering decisions and ensure healthy plant growth.

This project combines:
- 🧠 Python ML models (Random Forest, SVC)
- 📡 ESP32-based sensor monitoring (DHT11, soil moisture)
- 📱 Blynk cloud dashboard (remote control + visualization)
- 🔌 Relay-based irrigation automation

---

## 🔧 System Architecture

[Sensors - DHT11 + Moisture] → ESP32 → Blynk Cloud → Python Model
↓
Intelligent Prediction
↓
Pump Control via Relay



- ESP32 reads temperature, humidity, and soil moisture.
- Data is sent to Blynk cloud and visualized in a mobile app.
- A trained ML model running in Python fetches this data, predicts whether watering is needed, and sends control signals back to the ESP32.
- The pump is controlled via a relay circuit.

---

## 🎥 Project Demo

📽️ **[Click to Watch the Working Video](https://drive.google.com/file/d/1Nnkiw32Zi8sppOWD3NO8K4yI0WD1yNJu/view?usp=sharing)**  
> Real-time sensor monitoring, prediction, and relay-controlled pump action shown in action.

---

## 🚀 Features

- 📡 Real-time temperature, humidity, and moisture sensing
- 🔗 Blynk-powered cloud interface for data visibility and override
- 🧠 ML-based intelligent watering decisions (Random Forest & SVM)
- 🔁 Automated pump activation via relay switching
- 📱 Mobile app UI + dashboard integration
- 🛠️ Custom relay circuit and PCB layout included

---

## 📂 Project Files

| File Name                         | Description |
|----------------------------------|-------------|
| `verdant_decision.py`            | Python script fetching sensor data from Blynk, predicting, and sending decisions back |
| `gardening ecosystem.ipynb`      | Model training & testing notebook |
| `watering_modelRandomForest.pkl` | Trained Random Forest model |
| `watering_modelSVC.pkl`          | Trained SVM model |
| `Farm_Weather_Data.csv`          | Training dataset |
| `system_photo.jpg`               | Hardware setup photo |
| `relay.pdf`                      | Relay circuit diagram & explanation |
| `BLYNK APPLICATION.docx`         | Full guide to Blynk app usage |
| `VerdantVision_Sensor.ino.docx`  | ESP32 firmware code (DHT11 + moisture + relay) |
| `application_details.md`         | Description of Blynk app integration |
| `LICENSE`                        | MIT License |
| `README.md`                      | You're reading it! 🎉 |

---

## 🧠 ML Model Summary

- 📈 Target: Predict whether **watering is needed** (binary classification)
- 📊 Features used: MaxT, MinT, WindSpeed, Humidity, Precipitation
- 🧪 Models: Random Forest, SVC (sklearn)
- 🔄 Output used to trigger the relay (ON/OFF)

---

## 🛠 Hardware Used

- ESP32 Dev Board
- DHT11 Temperature & Humidity Sensor
- Soil Moisture Sensor (analog)
- Relay Module (custom transistor-based)
- Pump or Motor (as output actuator)

---

## 📱 Blynk Virtual Pin Mapping

| Virtual Pin | Usage                |
|-------------|----------------------|
| V0          | Temperature (°C)     |
| V1          | Humidity (%)         |
| V2          | Moisture Level (%)   |
| V3          | ML Decision (Pump ON/OFF) |
| V4          | Manual override button    |

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 👤 Author

**Ananya Ravi**  
🛠️ GitHub: [@Ananya1807](https://github.com/Ananya1807)  
📧 Email: ananyaravi1807@gmail.com  

---

> “Let your plants grow smarter.”
