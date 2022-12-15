from game.shared.color import Color

# The constants used througout the game.
VERSION = "1.3"

COLUMNS = 127
ROWS = 127
CELL_SIZE = 8
MAX_X = (COLUMNS+2) * CELL_SIZE
MAX_Y = (ROWS+2) * CELL_SIZE
FRAME_RATE = 29
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

1 = Insert down right glider at cursor.
2 = Insert up right glider at cursor.
3 = Insert down left glider at cursor.
4 = Insert up left glider at cursor.
5 = Randomize grid.
6 = Insert pattern "6"
"""