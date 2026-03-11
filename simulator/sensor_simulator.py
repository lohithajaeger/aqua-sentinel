import random
import requests
import time

url = "http://127.0.0.1:8000/sensor"

while True:

    data = {
        "temperature": round(random.uniform(20, 32), 2),
        "ph": round(random.uniform(6.5, 8.5), 2),
        "oxygen": round(random.uniform(180, 260), 2)
    }

    try:
        r = requests.post(url, json=data)
        print("Sent:", data)
        print("Prediction:", r.json())
    except Exception as e:
        print("Error:", e)

    print("----------------------------")

    time.sleep(5)