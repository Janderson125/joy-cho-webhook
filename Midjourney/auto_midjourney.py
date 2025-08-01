import pyautogui
import pyperclip
import time

# Load prompts from a text file
with open("prompts.txt", "r", encoding="utf-8") as file:
    prompts = [line.strip() for line in file if line.strip()]

# Countdown to allow switching to Discord window
print("You have 10 seconds to focus the Discord chat input box...")
time.sleep(10)

for prompt in prompts:
    full_prompt = f"/imagine prompt: {prompt}"
    print(f"Sending: {full_prompt}")

    pyperclip.copy(full_prompt)  # Copy to clipboard
    pyautogui.hotkey("ctrl", "v")  # Paste into Discord
    pyautogui.press("enter")       # Send the message

    time.sleep(5)  # Delay between prompts (adjust if needed)
