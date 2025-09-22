# benign_detection_demo.py
import json
from pathlib import Path
import requests
import time

OUTFILE = Path("harvest_simulation.txt")

def simulate_activity():
    OUTFILE.write_text("username: alice\npassword: hunter2\n")
    print("Wrote harvest file:", OUTFILE)

    try:
        payload = {"note": "benign demo", "file": OUTFILE.read_text()}
        resp = requests.post("http://127.0.0.1:8000/receive", json=payload, timeout=3)
        print("Posted to local server, status:", resp.status_code)
    except Exception as e:
        print("Local POST failed (expected if no server):", e)

if __name__ == "__main__":
    simulate_activity()
