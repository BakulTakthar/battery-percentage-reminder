import psutil
from plyer import notification

def batteryrange(frequency):

    battery = psutil.sensors_battery()
    print(battery)

    percent = battery.percent

    while True:
        battery = psutil.sensors_battery()
        current_percent = battery.percent
        change = current_percent - percent
        diff = abs(change)

        if diff >= frequency:
            notification.notify(
                title = "Current Battery Percentage",
                message = f"{str(current_percent)}% battery remaining ",
                timeout = 5
            )

            percent = current_percent

        continue