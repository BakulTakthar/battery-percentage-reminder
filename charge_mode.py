import psutil
from plyer import notification
import time
import sys

def charge_mode(target, stop_button):
    battery = psutil.sensors_battery()  # Update the battery information inside the loop
    current_percent = battery.percent
    print("Current battery percentage:", current_percent)

    print(f"OKAY! you will be reminded at {target} battery percentage")

    while True:
        battery = psutil.sensors_battery()  # Update the battery information inside the loop
        current_percent = battery.percent
        print("checking...")
        if current_percent <= target and not battery.power_plugged:
        
            notification.notify(
                title="Current Battery Percentage - Please plug in the charger",
                message=f"{current_percent}% battery remaining",
                timeout=50
            )
            print("done!")
            break
        
        if stop_button:
            sys.exit()
            
        time.sleep(30)
