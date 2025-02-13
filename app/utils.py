import requests

def fetch_character_id(character_name):
    """
    Fetch the character ID from an external service.

    params: character_name (str): The name of the character to fetch the ID for.
    returns: Character ID or error message
    """
    url = "https://the-one-api.dev/v2/character"  # The actual URL of the external service
    headers = {
        "Authorization": "Bearer 3DZRec9HNFn69urV6L_X"  # Replace YOUR_API_KEY with your actual API key
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for character in data['docs']:
                if character['name'].lower() == character_name.lower():
                    return character['_id']
            return f"Error: Character '{character_name}' not found."
        else:
            return f"Error: Failed to fetch character ID. Status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {str(e)}"

def fetch_quotes(character_name):
    """
    Fetch quotes from an external service.

    params: character_name (str): The name of the character to fetch quotes for.
    returns: List of quotes or error message
    """
    character_id = fetch_character_id(character_name)
    if "Error" in character_id:
        return [character_id]

    url = f"https://the-one-api.dev/v2/character/{character_id}/quote"  # The actual URL of the external service
    headers = {
        "Authorization": "Bearer 3DZRec9HNFn69urV6L_X"  # Replace YOUR_API_KEY with your actual API key
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return [quote['dialog'] for quote in data['docs']]  # Extracting the quotes (dialogs)
        else:
            return [f"Error: Failed to fetch quotes. Status code: {response.status_code}"]
    except requests.RequestException as e:
        return [f"Error: {str(e)}"]

# Example usage
print(fetch_quotes("Gimli"))  # Output: List of quotes or error message