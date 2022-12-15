from game.shared.color import Color

# The constants used througout the game.
VERSION = "1.2.1"

COLUMNS = 120
ROWS = 120
CELL_SIZE = 8
MAX_X = (COLUMNS+2) * CELL_SIZE
MAX_Y = (ROWS+2) * CELL_SIZE
FRAME_RATE = 17
FONT_SIZE = 16
CAPTION = "Life"
CELL_CHAR = "*"
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
MSG_PAUSED = "Press h for help."
MSG_RUNNING = "Press p to pause."

MSG_HELP = """
While game is running:
----------------------
p = (or Space) to pause game.

While game is paused:
---------------------
h = Display this help.
j = Move cursor left. (Arrow keys also work)
k = Move cursor right.
i = Move cursor up.
l = Move cursor down.
s = Set cell.
x = Clear cell.
p = Unpause and run game. (Enter and Space also work)
q = Quit.

1 = Randomize grid.
2 = Insert Glider at cursor.
"""