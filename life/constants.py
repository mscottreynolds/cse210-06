from game.shared.color import Color

# The constants used througout the game.
VERSION = 1.1

COLUMNS = 80
ROWS = 60
CELL_SIZE = 15
MAX_X = (COLUMNS+2) * CELL_SIZE
MAX_Y = (ROWS+2) * CELL_SIZE
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
STATE_QUIT = 'q'

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# Messages
MSG_PAUSED = "Press Enter to run.  Arrow keys to move cursor.  Space to set cell.  x to clear cell.  c to clear screen.  q to quit."
MSG_RUNNING = "Press p to pause."