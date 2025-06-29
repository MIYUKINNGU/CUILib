import os
import CUILib.Enums as Enums
import CUILib.Structs as Structs
import CUILib.Error as Error

_console_SCREEN_SIZE = Structs.ScreenSize(0, 0)
_isinitialized = False

def initialize(screen_width, screen_height):
    global _console_SCREEN_SIZE, _isinitialized
    if _isinitialized:
        raise Error.InitializeError()
    _console_SCREEN_SIZE = Structs.ScreenSize(screen_width, screen_height)
    _isinitialized = True
    clear()
    if os.name == "nt":
        import ctypes

        ENABLE_PROCESSED_OUTPUT = 0x0001
        ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
        
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        kernel32.SetConsoleMode(handle, MODE)

def clear():
    if not is_initialized():
        raise RuntimeError()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show(*line):
    global _console_SCREEN_SIZE
    if not is_initialized():
        raise RuntimeError()
    if len(line) != _console_SCREEN_SIZE.get_height():
        raise ValueError()
    for v in line:
        if len(v) < _console_SCREEN_SIZE.get_width():
            raise ValueError()
    
    set_cursor(1, 1)
    print(*line, sep="\n")

def set_cursor(l, v):
    if not is_initialized():
        raise RuntimeError()
    if not 0 < l <= _console_SCREEN_SIZE.get_height():
        raise ValueError()
    if not 0 < v <= _console_SCREEN_SIZE.get_width():
        raise ValueError()
    print(f"\033[{l};{v}H", end="")

def mainloop(Update):
    if not is_initialized():
        raise RuntimeError()
    try:
        while True:
            eventcode = Update()
            match eventcode:
                case Enums.MainloopEventCode.Exit_Mainloop:
                    return 0
    except KeyboardInterrupt:
        return 0

def is_initialized():
    return _isinitialized

def get_screen_size():
    if not is_initialized():
        raise RuntimeError()
    return _console_SCREEN_SIZE

def set_cursor_visible(visible):
    if visible:
        print("\033[?25h", end="")
    else:
        print("\033[?25l", end="")
