import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.conf import settings
from django.db import models

# Ensure Django settings are configured
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fellowships.settings')
django.setup()

from app.models import BattleOutcome

# Fetch data from the BattleOutcome table
battle_outcomes = BattleOutcome.objects.all()

# Prepare the data
data = []
for outcome in battle_outcomes:
    data.append({
        'character_attack': outcome.character.attacks,
        'character_defense': outcome.character.defense,
        'artifact_offense': outcome.artifact.offensive_property,
        'artifact_defense': outcome.artifact.defensive_property,
        'opponent_attack': outcome.opponent.attacks,
        'opponent_defense': outcome.opponent.defense,
        'coin_toss_win': 1 if outcome.coin_toss_result == 'win' else 0,
        'outcome': 1 if outcome.result == 'win' else 0
    })

df = pd.DataFrame(data)

# Split the data into features and labels
features = df.drop('outcome', axis=1)
labels = df['outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")

# Save the model to a file
MODEL_PATH = 'ml/models/artifact_recommender.pkl'
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")