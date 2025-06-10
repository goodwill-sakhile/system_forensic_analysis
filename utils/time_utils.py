# Time Utilities

from datetime import datetime

def current_timestamp():
    return datetime.now().isoformat()

def format_timestamp(ts):
    return datetime.fromisoformat(ts).strftime('%Y-%m-%d %H:%M:%S')