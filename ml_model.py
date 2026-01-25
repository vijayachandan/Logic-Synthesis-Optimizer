# ml_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    data = pd.read_csv("training_data.csv")

    X = data[['total_gates', 'depth']]
    y = data['cost']

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "cost_model.pkl")
    print("Model trained and saved!")


def predict_cost(features):
    model = joblib.load("cost_model.pkl")
    return model.predict([features])[0]


# ---------- TRAIN ----------
if __name__ == "__main__":
    train_model()
