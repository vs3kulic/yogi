import requests
import json

def call_ollama(prompt):
    """
    Sends a request to the Ollama API with the given prompt and handles streamed JSON responses.
    """
    url = "http://localhost:11434/api/generate"  # Ollama endpoint
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gemma3:1b",  # Replace with the model you want to use
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10, stream=True)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx

        # Process the streamed response line by line
        result = []
        for line in response.iter_lines():
            if line:  # Skip empty lines
                try:
                    json_line = json.loads(line)
                    result.append(json_line.get("response", ""))  # Extract the "response" field
                except json.JSONDecodeError:
                    return {"error": "Invalid JSON in streamed response", "raw_line": line.decode("utf-8")}

        # Combine all responses into a single string
        combined_response = " ".join(result)
        print("Ollama Response:", combined_response)  # Print the combined response
        return {"response": combined_response}

    except requests.RequestException as e:
        return {"error": str(e)}