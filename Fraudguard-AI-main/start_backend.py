"""Start the backend server from project root"""
import uvicorn
import sys
import os

# Ensure we're in the project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import the app
from backend.main import app

if __name__ == "__main__":
    print("=" * 50)
    print("Starting Fraud Detection API...")
    print("=" * 50)
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )

