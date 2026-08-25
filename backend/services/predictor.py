import joblib
from pathlib import Path
import pandas as pd

from services.preprocessing import DataPreprocessor


class FraudPredictor:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent.parent
        ARTIFACT_DIR = BASE_DIR / "artifacts"

        self.model = joblib.load(ARTIFACT_DIR / "xgboost_model.pkl")
        self.imputer = joblib.load(ARTIFACT_DIR / "imputer.pkl")
        self.feature_columns = joblib.load(ARTIFACT_DIR / "feature_columns.pkl")
        self.raw_input_columns = joblib.load(ARTIFACT_DIR / "raw_input_columns.pkl")

        self.preprocessor = DataPreprocessor()

    def predict(self, df):

        processed_df = self.preprocessor.transform(df)

        prediction = self.model.predict(processed_df)

        probability = self.model.predict_proba(
            processed_df
        )[:, 1]

        result = df.copy()

        result["Prediction"] = prediction

        result["Fraud_Probability"] = probability

        result["Prediction"] = result["Prediction"].map(
            {
                0: "Legitimate",
                1: "Fraud"
            }
        )

        return result