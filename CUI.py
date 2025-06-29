import CUILib.console as console
import CUILib.Error as Error
from CUILib.Enums import *

_isinitialized = False
_data = []
_screenmode = ScreenArea.Back_Screen
_half_width_mode = True
def initialize(screen_width, screen_height):
    global _isinitialized, _data
    if _isinitialized:
        raise Error.InitializeError()
    if console.is_initialized():
        screen_size = console.get_screen_size()
        if screen_size.get_width() != screen_width or screen_size.get_height() != screen_height:
            raise ValueError()
        _data = [[" " for _ in range(screen_width)] for i in range(screen_height)]
    else:
        console.initialize(screen_width, screen_height)
        _data = [[" " for _ in range(screen_width)] for i in range(screen_height)]
    _isinitialized = True

def textinput(x, y):
    console.set_cursor(x, y)
    return input()

def can_draw(x, y, data):
    if x < 1 or y < 1:
        return False
    if len(data) == 0:
        return False
    if y+len(data)-1 > console.get_screen_size().get_height():
        return False
    for i in range(len(data)):
        if x+len(data[i])-1 > console.get_screen_size().get_width():
            return False
        if _half_width_mode:
            for j in range(len(data[i])):
                if ord(data[i][j]) > 0xff:
                    return False
    return True                

def draw(x, y, data):
    global _half_width_mode, _data
    if not can_draw(x, y, data):
        raise ValueError()
    for i in range(len(data)):
        for j in range(len(data[i])):
            _data[y+i-1][x+j-1] = data[i][j]
    if not bool(_screenmode):
        console.show(*["".join(_data[i]) for i in range(len(_data))])

def set_halfwidth_mode(condition):
    global _half_width_mode
    _half_width_mode = condition

def set_draw_screen(area):
    global _screenmode
    _screenmode = area

def is_halfwidth_mode():
    global _half_width_mode
    return _half_width_mode

def is_draw_screen():
    global _screenmode
    return _screenmode

def screen_update():
    if _screenmode != ScreenArea.Back_Screen:
        raise RuntimeError("Back screen is not valid.")
    console.show(*["".join(_data[i]) for i in range(len(_data))])

def mainloop(Update):
    set_draw_screen(ScreenArea.Back_Screen)
    console.clear()
    def newUpdater():
        r = Update()
        console.set_cursor_visible(False)
        screen_update()
        console.set_cursor_visible(True)
        return r
    return console.mainloop(newUpdater)

def get_size():
    return console.get_screen_size()

def is_initialized():
    return _isinitialized