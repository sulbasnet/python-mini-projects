from datetime import datetime
import winsound
import time

# Take alarm time input
alarm_time = input("Enter alarm time in 24-hour format (HH:MM:SS): ")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]

print(f"Alarm set for {alarm_hour}:{alarm_minute}:{alarm_second}...")
print("Waiting for alarm time...")

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")

    if (alarm_hour == current_hour and
        alarm_minute == current_minute and
        alarm_second == current_second):
        print("Wake Up!!")
        for i in range(5):  
            winsound.Beep(1000, 500)
            time.sleep(0.5)
        break

    time.sleep(1)
