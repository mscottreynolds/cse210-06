from game.shared.color import Color

VERSION = 1.0

COLUMNS = 80
ROWS = 60
CELL_SIZE = 15
MAX_X = 1200
MAX_Y = 900
FRAME_RATE = 15
FONT_SIZE = 15
CAPTION = "Life"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
STATE_RUN = 'r'
STATE_PAUSE = 'p'
STATE_INITIAL = 'i'

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# Messages
MSG_PAUSED = "Press r to run. j, k, l, i to move cursor. s to set cell. x to clear cell."
MSG_RUNNING = "Press p to pause. Esc to quit."