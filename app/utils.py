import requests
from decouple import config

def fetch_quotes(character_id):
    """
    Fetch quotes from an external service.

    params: character_id (str): The ID of the character to fetch quotes for.
    returns: List of quotes or error message
    """
    url = f"https://the-one-api.dev/v2/character/{character_id}/quote"
    headers = {
        "Authorization": f"Bearer {config('API_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return [quote['dialog'] for quote in data['docs']]
        else:
            return [f"Error: Failed to fetch quotes. Status code: {response.status_code}"]
    except requests.RequestException as e:
        return [f"Error: {str(e)}"]

# Add a function to fetch and print all character names for debugging
def fetch_all_characters():
    url = "https://the-one-api.dev/v2/character"
    headers = {
        "Authorization": f"Bearer {config('API_BEARER_TOKEN')}"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for character in data['docs']:
                print(character['name'])
        else:
            print(f"Error: Failed to fetch characters. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {str(e)}")

