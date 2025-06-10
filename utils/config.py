# Configuration Manager

import json
import os

CONFIG_PATH = "config.json"

default_config = {
    "cpu_threshold": 80,
    "memory_threshold": 80,
    "disk_threshold": 90,
    "monitor_interval": 5
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'w') as f:
            json.dump(default_config, f, indent=4)
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)