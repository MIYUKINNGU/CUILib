from enum import Enum

class MainloopEventCode(Enum):
    Continue = 0
    Exit_Mainloop = 1

class ScreenArea(Enum):
    Real_Screen = 0
    Back_Screen = 1