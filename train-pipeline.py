import os
import subprocess
import sys
from datetime import datetime

def run_training():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    print(f"[{timestamp}] Starting training...")

    # Use the same Python environment
    subprocess.run([sys.executable, "train.py"], check=True)

    print(f"[{timestamp}] Training completed.")

if __name__ == "__main__":
    run_training()

