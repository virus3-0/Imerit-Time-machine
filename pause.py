import pyautogui
import time
from datetime import datetime

# Wait until 1:00 PM
target_time = "13:00"  # 1:00 PM in 24-hour format
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        break
    print(f"Waiting for the time... Current time: {current_time}")
    time.sleep(10)  # Check every 10 seconds

# Find the position of the pause button (You need to manually find it)
button_location = pyautogui.locateOnScreen("pause.png")  # Screenshot of the pause button
if button_location:
    pyautogui.click(button_location)  # Click the button
    print("Clicked the pause button successfully!")
else:
    print("pause button not found!")

# Keep the system idle for a few seconds before closing
time.sleep(5)
