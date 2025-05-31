def get_yoga_prompt(user_data):
    """
    Generates a prompt for Ollama based on user data.

    Args:
        user_data (dict): Data about the user (e.g., answers to the questionnaire).

    Returns:
        str: The generated prompt.
    """
    return f"""
    Based on the following user data, recommend a yoga practice:
    - Name: {user_data.get('name', 'Unknown')}
    - Age: {user_data.get('age', 'Unknown')}
    - Preferences: {', '.join(user_data.get('preferences', []))}

    Provide a detailed explanation and a personalized yoga routine.
    """