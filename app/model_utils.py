"""
Model loading and prediction logic.

The model must be loaded ONCE at module level, NOT inside the predict function.
"""

import joblib
import pickle
import pandas as pd


# TODO 1: Load your serialized churn model (and preprocessor if any) from data/
model = joblib.load("data/model.pkl")


def preprocess(features):
    with open("data/transformer.pkl", "rb") as f:
        transformer = pickle.load(f)

    df = pd.DataFrame(
        [features],
        columns=[
            "CreditScore",
            "Geography",
            "Gender",
            "Age",
            "Tenure",
            "Balance",
            "NumOfProducts",
            "HasCrCard",
            "IsActiveMember",
            "EstimatedSalary",
        ],
    )

    features = transformer.transform(df)
    return features


def predict_churn(features: list[float]) -> int:
    """
    Takes a list of raw feature values and returns a churn prediction (0 or 1).
    """
    # TODO 3: Preprocess the features
    processed_features = preprocess(features)

    # TODO 4: Use model.predict() on processed_features to get a prediction and return it as an int
    #         Hint: model.predict() expects a 2D array
    if model is not None:
        prediction = model.predict(processed_features)[0]
        return int(prediction)
    else:
        raise ValueError("Model is not loaded")


if __name__ == "__main__":
    # TODO 5: Replace with sample features that match your model
    sample = [
        619,
        "France",
        "Female",
        42,
        2,
        0.0,
        1,
        1,
        1,
        101348.88,
    ]
    print(f"Input:      {sample}")
    print(f"Prediction: {predict_churn(sample)}")
