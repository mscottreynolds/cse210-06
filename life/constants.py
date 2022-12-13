from game.shared.color import Color

# The constants used througout the game.
VERSION = 1.2

COLUMNS = 160
ROWS = 120
CELL_SIZE = 8
MAX_X = (COLUMNS+2) * CELL_SIZE
MAX_Y = (ROWS+2) * CELL_SIZE
FRAME_RATE = 29
FONT_SIZE = 16
CAPTION = "Life"
CELL_CHAR = "#"
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
STATE_RUN = 'r'
STATE_PAUSE = 'p'
STATE_INITIAL = 'i'
STATE_QUIT = 'q'

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# Messages
MSG_PAUSED = "Press j, k, i, l to move cursor.  Press r to run, s to set cell, x to clear cell, c to clear screen, and q to quit."
MSG_RUNNING = "Press p to pause."