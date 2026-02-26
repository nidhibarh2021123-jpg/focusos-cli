import time
import csv
from datetime import datetime

def focus_timer(minutes):
    try:
        seconds = int(minutes) * 60
    except ValueError:
        print("Please enter a valid number.")
        return

    print(f"Focus session started for {minutes} minute(s).")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nSession completed!")

    # Log session
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sessions.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([now, minutes])
    print("Session logged successfully.")

if __name__ == "__main__":
    minutes = input("Enter focus duration (in minutes): ")
    focus_timer(minutes)
