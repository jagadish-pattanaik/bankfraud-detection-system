import joblib
from pathlib import Path


# backend/
BASE_DIR = Path(__file__).resolve().parent.parent
ARTIFACT_DIR = BASE_DIR / "artifacts"


class FileValidator:

    def __init__(self):

        self.required_columns = joblib.load(
            ARTIFACT_DIR / "raw_input_columns.pkl"
        )

    def validate_extension(self, filename):

        allowed = (".csv", ".xlsx", ".xls")

        if not filename.lower().endswith(allowed):
            raise ValueError(
                "Only CSV, XLSX and XLS files are supported."
            )

    def validate_empty(self, df):

        if df.empty:
            raise ValueError(
                "Uploaded file is empty."
            )

    def validate_duplicate_headers(self, df):

        duplicates = df.columns[df.columns.duplicated()].tolist()

        if duplicates:
            raise ValueError(
                f"Duplicate column names found: {duplicates}"
            )

    def validate_required_columns(self, df):

        missing = [
            col
            for col in self.required_columns
            if col not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

    def validate(self, filename, df):

        self.validate_extension(filename)
        self.validate_empty(df)
        self.validate_duplicate_headers(df)
        self.validate_required_columns(df)

        return True