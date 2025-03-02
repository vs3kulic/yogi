import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate some example data
# Replace this with your actual data loading and preprocessing
data = {
    'character_attack': [10, 15, 7, 8, 12],
    'character_defense': [5, 7, 3, 4, 6],
    'artifact_offense': [3, 5, 2, 4, 3],
    'artifact_defense': [2, 3, 1, 2, 2],
    'opponent_attack': [8, 10, 6, 7, 9],
    'opponent_defense': [4, 5, 3, 4, 5],
    'coin_toss_win': [1, 0, 1, 0, 1],
    'outcome': [1, 0, 1, 0, 1]
}
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