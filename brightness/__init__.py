import re
import subprocess

def set(value: int):
    value = min(max(value, 0), 100)
    subprocess.run(["powershell.exe", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {value})"])

def get():
    try:
        command = "Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness"
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        match = re.search(r"CurrentBrightness\s+:\s+(\d+)", result.stdout)
        if match:
            value = int(match.group(1))
            return value
    except Exception as e:
        print(f"error: {e}")
    return None

def increase(value: int):
    value = min(max(value, 0), 100)
    subprocess.run(["powershell.exe", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {get() + value})"])

def decrease(value: int):
    value = min(max(value, 0), 100)
    subprocess.run(["powershell.exe", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {get() - value})"])