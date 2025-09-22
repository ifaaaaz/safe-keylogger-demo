# Safe Keylogger Demo — Educational Project

**Author:** MOHAMMED IFAZ M  
**Date:** 2025-09-22  

---

## Overview
This repository demonstrates a **consent-based in-app keylogger** and a **benign detection demo** using Python. The purpose of this project is **educational only**, to understand how keystroke logging works in a controlled environment and how such activity can be monitored and detected.  

> **Important:** No system-wide or stealth keylogging is included. All scripts run locally and require explicit user consent.

---

## Project Files

| File | Description |
|------|-------------|
| `safe_in_app_logger.py` | Tkinter-based GUI logger. Logs keystrokes typed **only inside the app window** after the user consents. Saves output to `in_app_keylog.txt`. |
| `benign_detection_demo.py` | Simulates a local "harvest" file and posts it to a local Flask server. Demonstrates benign exfiltration and detection. |
| `local_receiver.py` | Flask app that receives POSTs from `benign_detection_demo.py`. Only runs on localhost for demo purposes. |
| `.gitignore` | Excludes virtual environment, cache files, and other non-source files. |

---

## How to Run (Kali Linux / Linux)

## Notes

- Each script should run in a separate terminal.
- The in-app logger only records keys typed inside its own window after explicit consent.
- All logged data is sanitized for demonstration purposes.

**Activate the virtual environment:**

```bash
source venv/bin/activate


2. **Install dependencies**
```bash
pip install --upgrade pip
pip install flask requests

3. **Start the local receiver (Terminal 1)**
```bash
python local_receiver.py

4. **Run the benign detection demo (Terminal 2)**
```bash
python benign_detection_demo.py

5. **Run the GUI in-app logger (Terminal 3 — requires GUI/X session)**
```bash
python safe_in_app_logger.py

6. **Use the in-app GUI logger**  
Click **Start Logging (Consent)**, type some test text, then click **Stop Logging**.

## Ethics & Safety

- All work is **educational and local only**.
- No global/system keylogging or unauthorized data collection is included.
- Testing with real credentials or third-party systems is strictly prohibited without consent.

## Learning Outcomes

- Understand keyboard event handling in Python
- Learn how keystroke logging can be monitored and detected
- Practice safe, ethical experimentation in cybersecurity
- Gain awareness of ethical, legal, and technical considerations for sensitive data handling
