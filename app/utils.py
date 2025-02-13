import requests

def fetch_quotes():
    url = "https://api.example.com/quotes"  # Replace with the actual URL of the external service
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # Assuming the response is in JSON format
        else:
            return ["Error: Failed to fetch quotes."]
    except requests.RequestException as e:
        return [f"Error: {str(e)}"]
