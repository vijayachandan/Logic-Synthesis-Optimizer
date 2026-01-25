# test_ai_cost.py

from feature_extractor import extract_features
from cost_function import calculate_cost
from ml_model import predict_cost

expr = "(A & B) | (~A & C)"

features = extract_features(expr)
manual_cost = calculate_cost(expr)
ai_cost = predict_cost(features)

print("Features:", features)
print("Manual Cost:", manual_cost)
print("AI Predicted Cost:", round(ai_cost, 2))
