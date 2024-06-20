import pyautogui
import os
from datetime import datetime

def make_screenshot():
    screenshot = pyautogui.screenshot()
    folder_path = 'img'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_path = os.path.join(folder_path, f'screenshot_{timestamp}.png')
    screenshot.save(file_path)
    return file_path

