import winsound
import ctypes
from time import sleep
import win32con


#where you should limit your time
websites_to_kill = ['Facebook', 'Youtube']

# alert after this time
time_limit_stage_one = 30

# minimize the window after this time
time_limit_stage_two = 50

# killl chrome if nothing helps
time_limit_stage_three = 120

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
SendMessageA = ctypes.windll.user32.SendMessageA
CloseWindow = ctypes.windll.user32.CloseWindow

titles = []
wnds = []
i = 0

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        if 'Google Chrome' in buff.value:
            if any(w.lower() in str(buff.value).lower() for w in websites_to_kill):
                titles.append(buff.value)
                wnds.append(hwnd)
    return True


def alerter(i, wnds):
    if (i >= time_limit_stage_one) & (i < time_limit_stage_two):
        winsound.PlaySound('one.wav', winsound.SND_FILENAME)
        i += 10
    if (i >= time_limit_stage_two) & (i < time_limit_stage_three):
        CloseWindow(wnds[0])
        winsound.PlaySound('two.wav', winsound.SND_FILENAME)
        i += 2
    elif i >= time_limit_stage_three:
        SendMessageA(wnds[0], win32con.WM_CLOSE, 0, 0)
    return i


while True:
    sleep(1)
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    if titles:
        i += 1
        i = alerter(i, wnds)
        #i = k
        titles = []
        wnds = []
    else:
        i = 0
