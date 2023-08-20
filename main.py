from pynput import mouse, keyboard
import pygetwindow as gw
import threading
import psutil

current_word = 'a'

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
        print('{0}'.format(
            key))
        global current_word
        current_word = key.char
        if key.char == 'x':
            return False
    except AttributeError:
        print('{0}'.format(
            key))

def on_click_mouse(x, y, button, pressed):
    print('{0} {1} at {2}'.format(
        'Pressed' if pressed else 'Released',
        'Left' if button == mouse.Button.left else 'Right',
        (x, y)))
    if not pressed and button == mouse.Button.right:
        # Stop listener
        return False

if __name__ == "__main__":
    thread1 = threading.Thread(target=listeners)
    thread2 = threading.Thread(target=observers)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("tasks done")