import requests

url = "https://api.thinger.io/v3/users/nezuko/buckets/lake_data/data"

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJweXRob25fYXBpIiwic3ZyIjoiYXAtc291dGhlYXN0LmF3cy50aGluZ2VyLmlvIiwidXNyIjoibmV6dWtvIn0.SuFLmiq2oumFD1eLV42M6aVs90__7wqGq-zNS4lVvK8"

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "data": {
        "test": 123
    }
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)