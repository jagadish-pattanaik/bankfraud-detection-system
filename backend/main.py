from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse

from services.validator import FileValidator
from services.predictor import FraudPredictor
from utils.reader import FileReader

from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Bank Fraud Detection API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

validator = FileValidator()
predictor = FraudPredictor()

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

PREDICTION_FILE = OUTPUT_DIR / "prediction.csv"


@app.get("/")
def home():
    return {
        "message": "Bank Fraud Detection API is running."
    }


@app.post("/predict")
async def predict(request: Request, file: UploadFile = File(...)):

    try:

        # Validate uploaded file
        validator.validate_extension(file.filename)

        # Read file
        df = FileReader.read(file)

        # Validate dataframe
        validator.validate(file.filename, df)

        # Prediction
        result = predictor.predict(df)

        # Save prediction file
        # Generate a unique filename
        filename = f"{uuid4().hex}_prediction.csv"
        prediction_path = OUTPUT_DIR / filename

        # Save prediction
        result.to_csv(prediction_path, index=False)

        fraud_count = (result["Prediction"] == "Fraud").sum()
        legit_count = (result["Prediction"] == "Legitimate").sum()

        return {
            "status": "success",
            "message": "Prediction completed successfully.",
            "total_records": len(result),
            "fraud_accounts": int(fraud_count),
            "legitimate_accounts": int(legit_count),
            "download_url": str(
            request.url_for(
            "download_prediction",
            filename=filename
                )
            )
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.get("/download/{filename}")
def download_prediction(filename: str):

    prediction_path = OUTPUT_DIR / filename

    if not prediction_path.exists():
        return {
            "status": "error",
            "message": "Prediction file not found."
        }

    return FileResponse(
        path=prediction_path,
        media_type="text/csv",
        filename="prediction.csv"
    )