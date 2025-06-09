# File Storage for Reports

import os

REPORTS_DIR = "reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def save_report(name: str, content: str):
    with open(os.path.join(REPORTS_DIR, f"{name}.txt"), 'w') as f:
        f.write(content)