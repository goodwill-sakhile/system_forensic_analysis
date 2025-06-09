# Automation Script

from core.monitor import get_system_stats
from core.event_analyzer import analyze_event
from handlers.alert_handler import send_alert
from handlers.forensic_reporter import generate_report

def auto_run():
    stats = get_system_stats()
    alerts = analyze_event(stats)
    if alerts:
        for alert in alerts:
            send_alert(alert)
        generate_report(stats)