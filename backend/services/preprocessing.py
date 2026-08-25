import pandas as pd
import joblib
from pathlib import Path

# backend/
BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACT_DIR = BASE_DIR / "artifacts"


class DataPreprocessor:

    def __init__(
        self,
        feature_columns_path=None,
        num_imputer_path=None
    ):

        if feature_columns_path is None:
            feature_columns_path = ARTIFACT_DIR / "feature_columns.pkl"

        if num_imputer_path is None:
            num_imputer_path = ARTIFACT_DIR / "imputer.pkl"

        self.feature_columns = joblib.load(feature_columns_path)
        self.num_imputer = joblib.load(num_imputer_path)

    def transform(self, df):

        # Remove unnecessary columns
        df.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")

        # Remove fully-null columns
        # ONLY if they are not required
        full_null_cols = df.columns[df.isnull().all()]

        cols_to_drop = [
            col
            for col in full_null_cols
            if col not in self.feature_columns
        ]

        df.drop(columns=cols_to_drop, inplace=True)

        # Fill categorical missing values
        if "F3892" in df.columns:
            df["F3892"] = df["F3892"].fillna("Unknown")

        # Numeric median imputation
        num_cols = df.select_dtypes(include="number").columns

        if len(num_cols) > 0:
            df[num_cols] = self.num_imputer.transform(df[num_cols])

        # Date feature engineering
        if "F3888" in df.columns:

            df["F3888"] = pd.to_datetime(
                df["F3888"],
                errors="coerce"
            )

            df["Account_Year"] = df["F3888"].dt.year
            df["Account_Month"] = df["F3888"].dt.month

            df["Account_Age_Days"] = (
                pd.Timestamp.today() - df["F3888"]
            ).dt.days

            df.drop(columns=["F3888"], inplace=True)

        # Drop F2230 BEFORE encoding
        df.drop(columns=["F2230"], inplace=True, errors="ignore")

        # One-hot encode remaining categoricals
        categorical_cols = [
            "F3886",
            "F3889",
            "F3890",
            "F3891",
            "F3892",
            "F3893"
        ]

        existing = [
            c for c in categorical_cols
            if c in df.columns
        ]

        df = pd.get_dummies(
            df,
            columns=existing,
            drop_first=True,
            dtype=int
        )

        # Remove leakage feature
        df.drop(columns=["F3912"], inplace=True, errors="ignore")

        # Final column alignment
        df = df.reindex(
            columns=self.feature_columns,
            fill_value=0
        )

        return df