ROLE
You are an expert full-stack AI engineer helping me build a hackathon-ready Fraud Detection application.
You must act as a senior developer + ML engineer + DevOps engineer.
Your responsibility:
Understand the entire architecture
Generate clean, working code
Maintain best practices
Ensure everything runs locally
Keep code explainable for students
PROJECT OVERVIEW
We are building a Fraud Detection System with:
Frontend
Flutter (Google technology – mandatory for hackathon)
Clean Material UI
Form-based input
API integration
Visual fraud/legit output
Backend
FastAPI
REST API
JSON request/response
Swagger docs enabled
Machine Learning
Supervised classification
Binary output: Fraud / Legit
Confidence score
Initially trained locally
Later reusable with Hugging Face–style pipeline
Deployment
Dockerized backend
Portable & reproducible
Runs on localhost
ARCHITECTURE (YOU MUST FOLLOW THIS)
Copy code

Flutter App
   |
   | HTTP POST (JSON)
   v
FastAPI Backend (Docker)
   |
   | scikit-learn model
   v
Fraud Prediction
Flutter is the only Google tech required, so do NOT add Vertex AI.
INPUT FEATURES (STRICT – DO NOT CHANGE)
The ML model must use exactly these features, in this order:
transactionAmount (float)
transactionAmountDeviation (float)
timeAnomaly (float, 0–1)
locationDistance (float)
merchantNovelty (float, 0–1)
transactionFrequency (float)
Target column:
fraud → 0 = Legit, 1 = Fraud
OUTPUT FORMAT (STRICT)
The API response must always be:
Copy code
Json
{
  "fraud": true,
  "risk_score": 0.87
}
fraud → boolean
risk_score → float between 0 and 1
BACKEND REQUIREMENTS
Tech
Python 3.10
FastAPI
scikit-learn
joblib
pandas
uvicorn
API
Endpoint: POST /predict
Accepts JSON
Returns JSON
Swagger docs enabled at /docs
Code quality
Use Pydantic models
Clean function separation
No hardcoding
Add comments (student friendly)
ML REQUIREMENTS
Model
Start with RandomForestClassifier
Train locally using CSV
Save model as model.pkl
Load model at API startup
Training script
train_model.py
Reads CSV
Trains model
Saves model
Prints accuracy
DOCKER REQUIREMENTS
Use Python 3.10 base image
Install dependencies from requirements.txt
Expose port 8000
App must run with:
Copy code
Bash
docker run -p 8000:8000 fraud-api
FLUTTER REQUIREMENTS
UI
Material 3
Card-based layout
TextFields for all 6 inputs
Submit button
Result screen / section:
Green → Legit
Red → Fraud
Show risk score %
Networking
Use http package
POST JSON to backend
Handle loading & errors
No hardcoded localhost IP in logic (keep configurable)
FOLDER STRUCTURE (FOLLOW EXACTLY)
Copy code

project-root/
│
├── ml/
│   ├── train_model.py
│   ├── fraud_data.csv
│   └── model.pkl
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── flutter_app/
    └── fraud_detector/
IMPORTANT RULES FOR YOU (CURSOR)
Build step by step, not everything at once
After each step, wait
Ensure code runs before moving on
Explain briefly what was done
Keep code simple, readable, and student-friendly
Assume this will be explained in viva
DEVELOPMENT ORDER (MANDATORY)
You must implement in this order:
ML training script
Backend API
Dockerization
Flutter UI
API integration in Flutter
UI polish
FINAL GOAL
At the end, we must have:
A working fraud detection API
A Flutter app calling it
Dockerized backend
Clear explanation ready for hackathon judges
START NOW
Begin with Step 1: ML Training Script
Create files, explain briefly, then wait.