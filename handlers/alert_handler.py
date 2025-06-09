# Alert Handler

from core.logger import log_event

def send_alert(message: str, level: str = "ALERT"):
    # Could later integrate email, Slack, etc.
    log_event(level, message)
    print(f"[{level}] {message}")