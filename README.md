# Bank Fraud Detection System using Machine Learning

A full-stack Machine Learning application for detecting fraudulent bank accounts using an optimized XGBoost model. It combines a robust machine learning pipeline with a FastAPI backend and a React frontend to provide an end-to-end fraud detection solution.

---

## Overview

Financial fraud detection is a critical problem for banking institutions. This project aims to automatically classify banking records as **Legitimate** or **Fraudulent** using supervised machine learning.

The application allows users to upload banking datasets in CSV or Excel format through a web interface. The uploaded data is validated, preprocessed, passed through a trained XGBoost model, and the prediction results are returned as a downloadable CSV file.

---

## Problem Statement

The objective of this project is to develop a machine learning model capable of accurately identifying fraudulent banking records while minimizing false positives and false negatives.

The solution includes:

- Data validation
- Data preprocessing
- Feature engineering
- Model training and evaluation
- REST API deployment
- React-based user interface

---

## Dataset

The dataset is **not included** in this repository because of its large size.

Place the dataset in the following directory:

```text
data/
```

Example:

```text
bankfraud-detection-system/
│
├── data/
│   └── Banking_Cleaned.csv
│
├── backend/
├── frontend/
└── README.md
```
---

## Machine Learning Development Process

### Initial Model Training

Initially, an XGBoost classifier was trained on the processed dataset.

The model achieved nearly perfect evaluation metrics on the train-test split, including almost perfect accuracy, precision, recall, and F1-score.

Although these results appeared impressive, they were unrealistic for a fraud detection problem and indicated that the model was likely learning information that directly revealed the target variable.

---

### Identifying the Cause of Overfitting

To investigate the issue, feature relationships with the target variable (`F3924`) were analyzed.

During this investigation, two features were identified as sources of data leakage:

- **F2230**
- **F3912**

These features showed an unusually strong relationship with the target variable and allowed the model to predict fraud almost directly rather than learning meaningful patterns.

Both leakage features were removed from the training pipeline before retraining the models.

This significantly improved the reliability of the evaluation.

---

### Handling Class Imbalance

The dataset contained significantly fewer fraudulent records than legitimate records.

For Logistic Regression, class imbalance was handled using:

```python
class_weight="balanced"
```

This helped improve the model's ability to detect minority-class fraud samples.

---

### Models Evaluated

The following machine learning models were implemented and compared using the same preprocessing pipeline.

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

---

### Model Validation

Rather than relying on a single train-test split, the models were evaluated using Stratified K-Fold Cross Validation.

The following techniques were used:

- StratifiedKFold
- cross_val_score
- Mean F1 Score

This evaluation strategy provided a more reliable estimate of real-world model performance.

---

## Model Comparison

| Model | Validation Method | Mean F1 Score |
|--------|-------------------|--------------:|
| XGBoost Classifier | StratifiedKFold + cross_val_score | **0.8438** |
| Random Forest | StratifiedKFold + cross_val_score | 0.6280 |
| Logistic Regression | StratifiedKFold + cross_val_score | 0.4418 |

The XGBoost Classifier achieved the highest Mean F1 Score and was selected as the final production model.

---

## Machine Learning Pipeline

```
Raw Banking Dataset
        │
        ▼
Data Validation
        │
        ▼
Missing Value Handling
        │
        ▼
Feature Engineering
        │
        ▼
One-Hot Encoding
        │
        ▼
Column Alignment
        │
        ▼
Leakage Feature Removal
(F2230, F3912)
        │
        ▼
Model Training
(Logistic Regression
 Random Forest
 XGBoost)
        │
        ▼
Cross Validation
(Stratified K-Fold)
        │
        ▼
Best Model Selection
        │
        ▼
FastAPI Deployment
        │
        ▼
React Frontend
```

---

## Project Structure

```text
bankfraud-detection-system/

├── data/
│
├── backend/
│   ├── artifacts/
│   │   ├── feature_columns.pkl
│   │   ├── imputer.pkl
│   │   ├── raw_input_columns.pkl
│   │   └── xgboost_model.pkl
│   │
│   ├── outputs/
│   │
│   ├── services/
│   │   ├── predictor.py
│   │   ├── preprocessing.py
│   │   └── validator.py
│   │
│   ├── utils/
│   │   └── reader.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │   ├── images/
│   │   │   ├── icons/
│   │   │   └── logo.svg
│   │   │
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── UploadBox.jsx
│   │   │   ├── SummaryCards.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   ├── ErrorAlert.jsx
│   │   │   └── Footer.jsx
│   │   │
│   │   ├── pages/
│   │   │   └── Home.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   └── eslint.config.js
│
├── README.md
└── .gitignore
```

---

## Technology Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

### Backend

- FastAPI
- Uvicorn

### Frontend

- React
- Vite
- Axios
- React Dropzone
- Framer Motion
- Lucide React

---

## Backend Workflow

1. Upload CSV or Excel file.
2. Validate file format and required columns.
3. Preprocess the dataset.
4. Perform feature engineering.
5. Align features with the training pipeline.
6. Generate fraud predictions using the trained XGBoost model.
7. Save the prediction report.
8. Return prediction statistics and a download link.

---

## API Endpoints

### GET /

Returns API status.

### POST /predict

Accepts a CSV or Excel file and returns:

- Total records
- Fraudulent accounts
- Legitimate accounts
- Download URL for prediction report

### GET /download/{filename}

Downloads the generated prediction CSV.

---

## Running the Project

### Clone the Repository

```bash
git clone https://github.com/jagadish-pattanaik/bankfraud-detection-system.git

cd bankfraud-detection-system
```

---

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

## Future Improvements

- Model explainability using SHAP
- Docker containerization
- Cloud deployment
- Authentication and authorization
- Database integration
- Real-time prediction API
- Continuous model monitoring
- Automated model retraining pipeline

---

## Author

**Jagadish Prasad Pattanaik**

B.Tech in Electrical Engineering
Odisha University of Technology and Research (OUTR)

---

## License

This project is intended for educational and research purposes.