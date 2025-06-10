# System Information

import platform
import socket

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "release": platform.release(),
        "architecture": platform.architecture()
    }