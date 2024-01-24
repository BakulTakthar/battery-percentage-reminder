import psutil
from plyer import notification
import time
battery = psutil.sensors_battery()
print(battery)
target = int(input("what battery percent do you want to be notified at? \n\n\n\n >>"))



while True:
    current_percent = battery.percent
    if current_percent <= target and battery.power_plugged == False:
        notification.notify(
            title="Current Battery Percentage, please plug in the charger",
            message=f"{str(current_percent)}% battery remaining ",
            timeout=50
        )


        break
    time.sleep(30)

    # Add a delay or sleep here if needed
    # time.sleep(60)  # Uncomment and adjust the value if you want to check periodically
