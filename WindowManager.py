import CUILib.CUI as CUI
from CUILib.Window import Window
import CUILib.Error as Error
from collections import OrderedDict

_Windows: OrderedDict[str, Window] = OrderedDict()
_isinitialized = False
def initialize():
    global _isinitialized, _Windows
    if _isinitialized:
        raise Error.InitializeError()
    if not CUI.is_initialized():
        raise Error.InitializeError("In order to initialize WindowManager, CUI need be initialized.")
    CUI.set_halfwidth_mode(True)
    screen_size = CUI.get_size()
    _Windows["Base"] = Window("", 1, 1, screen_size.get_width(), screen_size.get_height(), False)

def show():
    for w in _Windows.values():
        w.show()

def register_window(name, window):
    if type(window) != Window:
        raise TypeError()
    if name in _Windows:
        raise KeyError()
    _Windows[name] = window

def move_front(name):
    _Windows.move_to_end(name)

def get_all_windows():
    return dict(_Windows)

def get_window(name):
    return _Windows[name]

def get_windows_count():
    return len(_Windows)

def pop_window(name):
    w = _Windows.pop(name)
    del w

def is_initilized():
    return _isinitialized