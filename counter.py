from pynput import mouse, keyboard
import pygetwindow as gw
import threading
import psutil
import json
from datetime import datetime
from pprint import pprint
import tkinter as tk
import data

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
        print("{0}".format(key))

    analyze_keypress(key)


def on_click_mouse(x, y, button, pressed):
    if window_closed:
        return False

    print(
        "{0} {1} at {2}".format(
            "Pressed" if pressed else "Released",
            "Left" if button == mouse.Button.left else "Right",
            (x, y),
        )
    )
    if button == mouse.Button.left:
        data.current_data.update({"lclick": data.current_data.get("lclick") + 1})
    elif button == mouse.Button.right:
        data.current_data.update({"rclick": data.current_data.get("rclick") + 1})


def main():
    thread1 = threading.Thread(target=listeners)
    thread2 = threading.Thread(target=tkwindow)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    listeners()

    result = []
    for key in data.current_data:
        result.append({"KeyLabel": key, "Count": data.current_data.get(key)})

    print("returned")
    return result


def get_current_day():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    if int(day) < 10:
        day = f"0{day}"

    print(f"{year}-{month}-{day}")

    return f"{year}-{month}-{day}"


def analyze_keypress(key):
    try:
        if key.char in data.pair_char_dict:
            data.current_data.update(
                {
                    data.pair_char_dict.get(key.char): data.current_data.get(
                        data.pair_char_dict.get(key.char)
                    )
                    + 1
                }
            )
        else:
            data.current_data.update({key.char: data.current_data.get(key.char) + 1})
    except:  # special keys
        if key in data.special_char_dict:
            data.current_data.update(
                {
                    data.special_char_dict.get(key): data.current_data.get(
                        data.special_char_dict.get(key)
                    )
                    + 1
                }
            )
        else:
            print(f"logging error - key: {key} not counted")


def update(target: dict, sample: list):
    for i in range(len(sample)):
        target["KeyPresses"][i]["Count"] += sample[i]["Count"]

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

if __name__ == "__main__":
    listeners()
