import pyautogui, time, keyboard
time.sleep(3)

running = False

def toggle_running():
    global running
    running = not running

keyboard.add_hotkey("f6", toggle_running)

while True:
    if running:
        pyautogui.click()
        time.sleep(0.01) # 0.01 for fern farm, 0.3 for mud farm
        pyautogui.rightClick()
        time.sleep(0.01) # 0.01 for fern farm, 0.3 for mud farm
    else:
        time.sleep(0.1)