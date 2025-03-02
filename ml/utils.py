import joblib
import pandas as pd
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models/artifact_recommender.pkl')
model = joblib.load(MODEL_PATH)

def preprocess_input(character, opponent, artifact, coin_toss_result):
    """Preprocess input data to match training pipeline."""
    coin_toss_win = 1 if coin_toss_result == 'win' else 0
    input_data = pd.DataFrame({
        'character_attack': [character.attacks],
        'character_defense': [character.defense],
        'artifact_offense': [artifact.offensive_property],
        'artifact_defense': [artifact.defensive_property],
        'opponent_attack': [opponent.attacks],
        'opponent_defense': [opponent.defense],
        'coin_toss_win': [coin_toss_win]
    })
    return input_data

def recommend_artifact(character, opponent, artifact, coin_toss_result):
    """Generate artifact recommendations based on input parameters."""
    input_data = preprocess_input(character, opponent, artifact, coin_toss_result)
    probability = model.predict_proba(input_data)[0][1]  # Probability of winning
    return probability