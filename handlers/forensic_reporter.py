# Forensic Reporter

from storage.file_storage import save_report
from utils.time_utils import current_timestamp

def generate_report(data: dict, report_name=None):
    if not report_name:
        report_name = f"report_{current_timestamp().replace(':', '-')}"
    content = "\n".join([f"{k}: {v}" for k, v in data.items()])
    save_report(report_name, content)
    return report_name