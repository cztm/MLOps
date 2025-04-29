# test_app.py
import requests
import json

url = "http://127.0.0.1:8000/predict"
headers = {"Content-Type": "application/json"}

payload = {
    "gender": "Male",
    "marital_status": "Yes",
    "anxiety": "Yes",
    "panic_attack": "No",
    "sought_specialist": "Yes"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Prediction:", response.json())

