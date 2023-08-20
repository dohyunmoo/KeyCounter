from pynput import mouse, keyboard

def main():
    mouse_listener = mouse.Listener(on_click=on_click_mouse)
    key_listener = keyboard.Listener(on_press=on_press_keyboard)

    mouse_listener.start()
    key_listener.start()

    mouse_listener.join()
    key_listener.join()

def on_press_keyboard(key):
    print('{0}'.format(
        key))
    if key.char == 'x':
        return False

def on_click_mouse(x, y, button, pressed):
    print('{0} {1} at {2}'.format(
        'Pressed' if pressed else 'Released',
        'Left' if button == mouse.Button.left else 'Right',
        (x, y)))
    if not pressed and button == mouse.Button.right:
        # Stop listener
        return False

if __name__ == "__main__":
    main()