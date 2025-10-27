import requests

# URL bilkul same hai (kyunki humne port map kiya hai)
url = "http://127.0.0.1:8000/predict"

# Yeh wahi client data hai jo Q6 mein diya hai
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

try:
    response = requests.post(url, json=client)
    print(response.json())
except requests.exceptions.ConnectionError:
    print("\nError: Connect nahi ho raha. Kya aapka Docker container chal raha hai?")