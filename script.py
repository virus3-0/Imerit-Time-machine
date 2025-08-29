import pyautogui
import time
from datetime import datetime

def wait_until_exact(target_time):
    """Wait until the specified target time (24-hour format, including seconds)."""
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == target_time:
                break
            print(f"⏳ Waiting for the exact time {target_time}... Current time: {current_time} 🕒")
            time.sleep(0.5)  # Check every half-second for higher precision
        print(f"🎯 BOOM! It's exactly {target_time}! Let's roll! 🚀")
    except Exception as e:
        print(f"❌ Error while waiting for the exact time: {e}")

def click_button_exact(image_path, button_name):
    """Locate and click a button on the screen using an image at the exact time."""
    try:
        # Save the current mouse position
        original_position = pyautogui.position()

        # Locate the button and click it
        button_location = pyautogui.locateOnScreen(image_path)  # Locate the button image on the screen
        if button_location:
            pyautogui.click(button_location)  # Click the button
            print(f"✅ Clicked the {button_name} button successfully! 🎉✨")
        else:
            print(f"❌ Oops! The {button_name} button is hiding from me! 🕵️‍♂️🔍")
        
        # Restore the mouse to its original position
        pyautogui.moveTo(original_position)
        print(f"🐭 Mouse pointer safely returned to its original position: {original_position} 🛡️")
    except pyautogui.FailSafeException:
        print("⚠️ PyAutoGUI Fail-Safe triggered. Move your mouse to the corner of the screen to stop the script. 🚨")
    except Exception as e:
        print(f"❌ Error while trying to click the {button_name} button: {e}")

try:
    # Step 1: Get the current time and decide the workflow
    current_time = datetime.now().strftime("%H:%M:%S")
    task_1_time = "13:00:00"  # 1:00 PM
    task_2_time = "14:00:00"  # 2:00 PM

    if current_time < task_1_time:
        # Wait until 1:00 PM and click the pause button
        print("🕒 Starting script before 1:00 PM...")
        wait_until_exact(task_1_time)  # Wait for 1:00 PM
        click_button_exact("pause.png", "pause")

        # Wait until 2:00 PM and click the resume button
        wait_until_exact(task_2_time)  # Wait for 2:00 PM
        click_button_exact("resume.png", "resume")

    else:
        # Start after 1:00 PM and directly perform the resume action
        print("⚠️ Starting script after 1:00 PM... Performing resume action immediately!")
        wait_until_exact(task_2_time)  # Wait for 2:00 PM before clicking resume
        click_button_exact("resume.png", "resume")

    # Keep the system idle for a few seconds before closing
    time.sleep(5)
    print("🎉 Mission accomplished! Everything worked like a charm! ✨💻")

except KeyboardInterrupt:
    print("🚨 Script interrupted by the user. Exiting gracefully! ✋")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")