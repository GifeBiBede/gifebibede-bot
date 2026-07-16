from enum import Enum

class State(Enum):
    IDLE = 0
    WAIT_GIF = 1
    WAIT_CODE = 2
    WAIT_DELETE = 3
    WAIT_EDIT = 4
