from pynput import mouse, keyboard
import pygetwindow as gw
import threading
import psutil
import json
from datetime import datetime

current_data = {
    'lclick': 0,
    'rclick': 0,
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0,
    '`': 0,
    'F1': 0,
    'F2': 0,
    'F3': 0,
    'F4': 0,
    'F5': 0,
    'F6': 0,
    'F7': 0,
    'F8': 0,
    'F9': 0,
    'F10': 0,
    'F11': 0,
    'F12': 0,
    'TAB': 0,
    'CAPSLOCK': 0,
    'SHIFT': 0,
    'CTRL': 0,
    'ALT': 0,
    'ESC': 0,
    'ENTER': 0,
    'UP': 0,
    'DOWN': 0,
    'LEFT': 0,
    'RIGHT': 0,
    'PRINTSCREEN': 0,
    'PAUSE': 0,
    'INSERT': 0,
    'HOME': 0,
    'PAGEUP': 0,
    'PAGEDOWN': 0,
    'DELETE': 0,
    'END': 0,
    'SCROLLLOCK': 0,
    'BACKSPACE': 0,
    '-': 0,
    '=': 0,
    '[': 0,
    ']': 0,
    '\\': 0,
    ';': 0,
    '\'': 0,
    ',': 0,
    '.': 0,
    '/': 0,
    'SPACE': 0
}

def observers():
    prev_active_window = gw.getActiveWindow()

    while True:
        active_window = gw.getActiveWindow()

        if active_window and active_window != prev_active_window:
            prev_active_window = active_window
            print(f"{active_window.title} at {id(active_window)}")

    return

def listeners():
    mouse_listener = mouse.Listener(on_click=on_click_mouse)
    key_listener = keyboard.Listener(on_press=on_press_keyboard)

    mouse_listener.start()
    key_listener.start()

    mouse_listener.join()
    key_listener.join()

def on_press_keyboard(key):
    try:
        print(f"{key.char}: {ord(key.char)}")
        if key.char == 'x':
            return False
    except:
        print('{0}'.format(
            key))
        
    analyze_keypress(key)

def on_click_mouse(x, y, button, pressed):
    print('{0} {1} at {2}'.format(
        'Pressed' if pressed else 'Released',
        'Left' if button == mouse.Button.left else 'Right',
        (x, y)))
    if not pressed and button == mouse.Button.right:
        # Stop listener
        return False
    
def main():
    # thread1 = threading.Thread(target=listeners)
    # thread2 = threading.Thread(target=observers)

    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

    listeners()

def get_current_day():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    return f"{year}-{month}-{day}"

def analyze_keypress(key):
    pass

def test(window):
    for i in psutil.pids():
        print(psutil.Process(i).name())
    # process = psutil.Process(pid)
    # executable_path = process.exe()

    # if "chrome.exe" in executable_path.lower():
    #     return "Chrome"
    # elif "code.exe" in executable_path.lower():
    #     return "VS Code"
    # else:
    #     return "Unknown"

    
if __name__ == "__main__":
    # get_current_day()
    main()
    today_date = get_current_day()

    with open('key_data.json', 'r') as js:
        js_obj = json.load(js)
    
    if js_obj.get(today_date) != None:
        print("exists")
    else:
        js.close()
        new_json = {today_date: current_data}
        with open('key_data.json', 'w') as js:
            json.dump(new_json, js, indent=4)

    # active_window = gw.getActiveWindow()

    # if active_window:
    #     window_type = test(active_window)
    #     print("Active window type:", window_type)
    # else:
    #     print("No active window found.")


    print("tasks done")
