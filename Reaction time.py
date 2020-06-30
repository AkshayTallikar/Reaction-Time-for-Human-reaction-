import win32api
import win32con
from PIL import ImageGrab


def click_green():
    green = ImageGrab.grab()
    px = green.load()
    middle = px.__getitem__((765, 265))
    if middle == (75, 219, 106):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 765, 265, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 765, 265, 0, 0)


while True:
    click_green()
