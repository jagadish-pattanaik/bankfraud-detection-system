import pandas as pd


class FileReader:

    @staticmethod
    def read(file):

        filename = file.filename.lower()

        if filename.endswith(".csv"):
            return pd.read_csv(file.file)

        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            return pd.read_excel(file.file)

        else:
            raise ValueError(
                "Unsupported file format. Upload CSV or Excel."
            )