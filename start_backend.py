import subprocess
import os
import sys
from threading import Thread

def run_command(command, cwd=None):
    """Run a shell command in the specified directory"""
    process = subprocess.Popen(
        command,
        shell=True,
        cwd=cwd,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    return process

if __name__ == "__main__":
    # Start backend API
    api_process = run_command("uvicorn main:app --reload --port 8000", 
                            cwd="backend")
    
    # Start explanation service
    explainer_process = run_command("python main.py",
                                  cwd="backend/explanation_service")
    
    try:
        # Keep the script running
        api_process.wait()
        explainer_process.wait()
    except KeyboardInterrupt:
        print("\nShutting down services...")
        api_process.terminate()
        explainer_process.terminate()