import pyautogui
import time
from datetime import datetime

# Wait until 2:00 PM
target_time = "14:17"  # 2:00 PM in 24-hour format
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        break
    print(f"Waiting for the time... Current time: {current_time}")
    time.sleep(10)  # Check every 10 seconds

# Find the position of the resume button (You need to manually find it)
button_location = pyautogui.locateOnScreen("resume.png")  # Screenshot of the resume button
if button_location:
    pyautogui.click(button_location)  # Click the button
    print("Clicked the resume button successfully!")
else:
    print("resume button not found!")

# Keep the system idle for a few seconds before closing
time.sleep(5)