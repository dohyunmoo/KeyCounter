from pynput import mouse, keyboard
import pygetwindow as gw
import threading
import psutil
import json
from datetime import datetime
from pprint import pprint
import tkinter as tk

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
    'SPACE': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '0': 0,
    'WIN': 0,
    'ALT': 0
}
special_char_dict = {
    keyboard.Key.space: 'SPACE',
    keyboard.Key.tab: 'TAB',
    keyboard.Key.caps_lock: 'CAPSLOCK',
    keyboard.Key.shift: 'SHIFT',
    keyboard.Key.ctrl_l: 'CTRL',
    keyboard.Key.backspace: 'BACKSPACE',
    keyboard.Key.enter: 'ENTER',
    keyboard.Key.esc: 'ESC',
    keyboard.Key.delete: 'DELETE',
    keyboard.Key.end: 'END',
    keyboard.Key.page_down: 'PAGEDOWN',
    keyboard.Key.page_up: 'PAGEUP',
    keyboard.Key.home: 'HOME',
    keyboard.Key.print_screen: 'PRINTSCREEN',
    keyboard.Key.scroll_lock: 'SCROLLLOCK',
    keyboard.Key.insert: 'INSERT',
    keyboard.Key.pause: 'PAUSE',
    keyboard.Key.up: 'UP',
    keyboard.Key.down: 'DOWN',
    keyboard.Key.left: 'LEFT',
    keyboard.Key.right: 'RIGHT',
    keyboard.Key.alt_l: 'ALT',
    keyboard.Key.cmd: 'WIN',
    keyboard.Key.f1: 'F1',
    keyboard.Key.f2: 'F2',
    keyboard.Key.f3: 'F3',
    keyboard.Key.f4: 'F4',
    keyboard.Key.f5: 'F5',
    keyboard.Key.f6: 'F6',
    keyboard.Key.f7: 'F7',
    keyboard.Key.f8: 'F8',
    keyboard.Key.f9: 'F9',
    keyboard.Key.f10: 'F10',
    keyboard.Key.f11: 'F11',
    keyboard.Key.f12: 'F12'
}
pair_char_dict = {
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z',
    '~': '`',
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5',
    '^': '6',
    '&': '7',
    '*': '8',
    '(': '9',
    ')': '0',
    '_': '-',
    '+': '=',
    '{': '[',
    '}': ']',
    '|': '\\',
    ':': ';',
    '"': '\'',
    '<': ',',
    '>': '.',
    '?': '/'
}

window_closed = False

# def observers():
#     prev_active_window = gw.getActiveWindow()

#     while True:
#         active_window = gw.getActiveWindow()

#         if active_window and active_window != prev_active_window:
#             prev_active_window = active_window
#             print(f"{active_window.title} at {id(active_window)}")

#     return

def listeners():
    mouse_listener = mouse.Listener(on_click=on_click_mouse)
    key_listener = keyboard.Listener(on_press=on_press_keyboard)

    mouse_listener.start()
    key_listener.start()

    mouse_listener.join()
    key_listener.join()

def on_press_keyboard(key):
    if window_closed:
        return False
    
    try:
        print(f"{key.char}: {ord(key.char)}")
    except Exception as e:
        print(f"Error: {str(e)}")
        print('{0}'.format(
            key))
        
    analyze_keypress(key)

def on_click_mouse(x, y, button, pressed):
    if window_closed:
        return False
    
    print('{0} {1} at {2}'.format(
        'Pressed' if pressed else 'Released',
        'Left' if button == mouse.Button.left else 'Right',
        (x, y)))
    if button == mouse.Button.left:
        current_data.update({'lclick': current_data.get('lclick') + 1})
    elif button == mouse.Button.right:
        current_data.update({'rclick': current_data.get('rclick') + 1})
    
def main():
    thread1 = threading.Thread(target=listeners)
    thread2 = threading.Thread(target=tkwindow)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    listeners()

    result = []
    for key in current_data:
        result.append({
            "KeyLabel": key,
            "Count": current_data.get(key)
        })
    
    print("returned")
    return result

def get_current_day():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    if int(day) < 10:
        day = f'0{day}'

    print(f"{year}-{month}-{day}")

    return f"{year}-{month}-{day}"

def analyze_keypress(key):
    try:
        if key.char in pair_char_dict:
            current_data.update({pair_char_dict.get(key.char): current_data.get(pair_char_dict.get(key.char)) + 1})
        else:
            current_data.update({key.char: current_data.get(key.char) + 1})
    except: # special keys
        if key in special_char_dict:
            current_data.update({special_char_dict.get(key): current_data.get(special_char_dict.get(key)) + 1})
        else:
            print(f"logging error - key: {key} not counted")

def update(target: dict, sample: list):
    for i in range(len(sample)):
        target['KeyPresses'][i]['Count'] += sample[i]['Count']
    
    return target

def tkwindow():
    def onClosing():
        global window_closed
        window_closed = True
        window.destroy()

    window = tk.Tk()
    window.title("Key Counter")
    window.geometry("200x100")

    tk.Label(window, text="Close this window to stop counting").pack()

    window.protocol("WM_DELETE_WINDOW", onClosing)

    window.mainloop()

    if window_closed:
        print("Closed")    

# def test(window):
#     for i in psutil.pids():
#         print(psutil.Process(i).name())
#     process = psutil.Process(pid)
#     executable_path = process.exe()
#
#     if "chrome.exe" in executable_path.lower():
#         return "Chrome"
#     elif "code.exe" in executable_path.lower():
#         return "VS Code"
#     else:
#         return "Unknown"

if __name__ == '__main__':
    listeners()