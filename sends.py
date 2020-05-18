import win32api
import win32con


def send_key(handle, key):
    win32api.PostMessage(handle, win32con.WM_KEYDOWN, key_to_hex(key), 0)
    win32api.PostMessage(handle, win32con.WM_KEYUP, key_to_hex(key), 0)


def send_mouse(handle, key, x, y):
    lParam = y << 16 | x
    if key == 'LM':
        win32api.PostMessage(
            handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam
        )
        win32api.PostMessage(handle, win32con.WM_LBUTTONUP, 0, lParam)
    elif key == 'RM':
        win32api.PostMessage(
            handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam
        )
        win32api.PostMessage(handle, win32con.WM_RBUTTONUP, 0, lParam)


def send_mousemove(handle, x, y):
    lParam = y << 16 | x
    win32api.PostMessage(handle, win32con.WM_MOUSEMOVE, 0, lParam)


def key_to_hex(key):
    switcher = {
        '0': 0x30,
        '1': 0x31,
        '2': 0x32,
        '3': 0x33,
        '4': 0x34,
        '5': 0x35,
        '6': 0x36,
        '7': 0x37,
        '8': 0x38,
        '9': 0x39,
        'a': 0x41,
        'b': 0x42,
        'c': 0x43,
        'd': 0x44,
        'e': 0x45,
        'f': 0x46,
        'g': 0x47,
        'h': 0x48,
        'i': 0x49,
        'j': 0x4A,
        'k': 0x4B,
        'l': 0x4C,
        'm': 0x4D,
        'n': 0x4E,
        'o': 0x4F,
        'p': 0x50,
        'q': 0x51,
        'r': 0x52,
        's': 0x53,
        't': 0x54,
        'u': 0x55,
        'v': 0x56,
        'w': 0x57,
        'x': 0x58,
        'y': 0x59,
        'z': 0x5A,
        'enter': 0x0D,
        'esc': 0x1B,
        'space': 0x20,
        'shift': 0x60,
    }
    return switcher.get(key, 0x0)
