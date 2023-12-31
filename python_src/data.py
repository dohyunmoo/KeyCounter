from pynput import mouse, keyboard

current_data = {
    "lclick": 0,
    "rclick": 0,
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    "`": 0,
    "F1": 0,
    "F2": 0,
    "F3": 0,
    "F4": 0,
    "F5": 0,
    "F6": 0,
    "F7": 0,
    "F8": 0,
    "F9": 0,
    "F10": 0,
    "F11": 0,
    "F12": 0,
    "TAB": 0,
    "CAPSLOCK": 0,
    "SHIFT": 0,
    "CTRL": 0,
    "ALT": 0,
    "ESC": 0,
    "ENTER": 0,
    "UP": 0,
    "DOWN": 0,
    "LEFT": 0,
    "RIGHT": 0,
    "PRINTSCREEN": 0,
    "PAUSE": 0,
    "INSERT": 0,
    "HOME": 0,
    "PAGEUP": 0,
    "PAGEDOWN": 0,
    "DELETE": 0,
    "END": 0,
    "SCROLLLOCK": 0,
    "BACKSPACE": 0,
    "-": 0,
    "=": 0,
    "[": 0,
    "]": 0,
    "\\": 0,
    ";": 0,
    "'": 0,
    ",": 0,
    ".": 0,
    "/": 0,
    "SPACE": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "0": 0,
    "WIN": 0,
    "ALT": 0,
}
special_char_dict = {
    keyboard.Key.space: "SPACE",
    keyboard.Key.tab: "TAB",
    keyboard.Key.caps_lock: "CAPSLOCK",
    keyboard.Key.shift: "SHIFT",
    keyboard.Key.ctrl_l: "CTRL",
    keyboard.Key.backspace: "BACKSPACE",
    keyboard.Key.enter: "ENTER",
    keyboard.Key.esc: "ESC",
    keyboard.Key.delete: "DELETE",
    keyboard.Key.end: "END",
    keyboard.Key.page_down: "PAGEDOWN",
    keyboard.Key.page_up: "PAGEUP",
    keyboard.Key.home: "HOME",
    keyboard.Key.print_screen: "PRINTSCREEN",
    keyboard.Key.scroll_lock: "SCROLLLOCK",
    keyboard.Key.insert: "INSERT",
    keyboard.Key.pause: "PAUSE",
    keyboard.Key.up: "UP",
    keyboard.Key.down: "DOWN",
    keyboard.Key.left: "LEFT",
    keyboard.Key.right: "RIGHT",
    keyboard.Key.alt_l: "ALT",
    keyboard.Key.cmd: "WIN",
    keyboard.Key.f1: "F1",
    keyboard.Key.f2: "F2",
    keyboard.Key.f3: "F3",
    keyboard.Key.f4: "F4",
    keyboard.Key.f5: "F5",
    keyboard.Key.f6: "F6",
    keyboard.Key.f7: "F7",
    keyboard.Key.f8: "F8",
    keyboard.Key.f9: "F9",
    keyboard.Key.f10: "F10",
    keyboard.Key.f11: "F11",
    keyboard.Key.f12: "F12",
}
pair_char_dict = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
    "~": "`",
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
    "_": "-",
    "+": "=",
    "{": "[",
    "}": "]",
    "|": "\\",
    ":": ";",
    '"': "'",
    "<": ",",
    ">": ".",
    "?": "/",
}
