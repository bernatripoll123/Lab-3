"""
Connect 4 — Template for Lab2 (Introduction to Programming)

Submission:
- Single python file: PNNN_TNN_P3_U1_U2.py
- Must run locally with: `python PNNN_TNN_P2_U1_U2.py`

Restrictions / Style rules:
- Requires pygame (install with `pip install pygame` if not already there)
- Yes `list`, `tuple`. No `class`, no `dict` or any structure we haven't seen in class
- This time we don't provide the signature of any function. You decide the structure of the program!
- All functions should receive the information they need as parameters, no global variables!
- For this reason, you might need to define some variable in the main function, before starting the main loop
- The rendering section is fully fucntional and provided in the main loop; there's no need to change it
- But you will need to add all the game logic

Anti-AI-copy/paste control:
- You must be able to explain to the professor all your code
- You must be able to explain specific sections of your program to the professor to verify your understanding

What code is provided:
A simple but fully functional view in pygame so students can focus on the model and the game logic.
The view pygame part:
- draws the empty board
- maps mouse clicks in the top strip to a column index for detecting a col from user
- draws a token on a specific (col,row) when asked
All the logic needs to be implemented by the students

What you need to implement:
Inside main():
- before entering the main loop and before initializing pygame call get_config() and ask user if modifying conditions
- within the main loop, you need to implement all the game logic
- DO IT ALL IN A WELL-STRUCTURED WAY
- DEFINE AND CALL AS MANY FUNCTIONS AS YOU THINK CONVENIENT

Outside main:
define all the functions that are called:
- for configuration (get_config() and called from there)
- for handling all the game logic
"""

import sys
import pygame
from random import randint

# =========================
# Board & UI configuration
# =========================

# no need to change any constant here - you can do it at your own risk
# if changing any of these options in get_config(), create a new variable - don't overwrite any constant
COLS = 7
ROWS = 6
CELL_SIZE = 100            # pixels per cell
GRID_LINE = 6              # thickness of the board grid lines
PADDING = 40               # outer padding around the board
TOKEN_MARGIN = 10          # inner margin within a cell for token radius
SELECT_STRIP_HEIGHT = 60   # clickable strip above the board for column selection

WIDTH = PADDING * 2 + COLS * CELL_SIZE
HEIGHT = PADDING * 2 + ROWS * CELL_SIZE + SELECT_STRIP_HEIGHT

# Some predefined Colors (RGB)
# You can create your own if you want (do it from get_config())
BG = (20, 24, 28)
BOARD_BG = (35, 60, 120)
GRID_COLOR = (15, 35, 85)
EMPTY_COLOR = (12, 16, 22)
RED = (220, 50, 47)
YELLOW = (253, 216, 53)
WHITE = (240, 240, 240)

# =========================
# Geometry (view-only)
# =========================
# better not touch anything
BOARD_LEFT = PADDING
BOARD_TOP = PADDING + SELECT_STRIP_HEIGHT
BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

# =========================
# Globals (view-only)
# =========================
screen = None   # for pygame

# =========================
# Write your functions here !!!!!!!!
# =========================w_

# Part 1: Configuration (called before starting the main loop)
def get_config():
    """ TODO STUDENTS: Currently does NOTHING. Should ask user if modifying conditions, such as:
    - 2 humans or human vs. machine
    - players' 2 colors
    - board size (optional)
    - whatever else you want ... (optional)
        
    Should return whatever has changed (do NOT use global variables)

    You are VERY encouraged to reuse functions from lab2, whenever possible, such as:
    * ask_yes_no()
    * read_int_in_range()
    * read_int_in_range_w_default()
    * change_colors()
    * read_color()
    """

    # TODO: add all the code needed
    return None

# define here all extra functions needed for config
# keep things clean, clear and well structured

# ==============================================
# Part 2: Game logic (called from the main loop)

# Define as many functions as you esteem convenient, 
# in order to keep things clean, clear and well structured


def paint_piece_demo(col):
    """ This code is just for showing how to use place_piece()
    place_piece() draws a token of a given color, in a given position (col and row)
    In this demo we just use random values (modify/eliminate this!)"""
    
    rand_row = randint(0,ROWS-1) # random row
    rand_color = (randint(0,255),randint(0,255),randint(0,255)) # random color
    print(f"col:{col}, row:{rand_row}, color:{rand_color}")
    place_piece(col, rand_row, rand_color)



# ========================================
# View helpers - No need to change anything
# ========================================

def cell_center(col, row):
    """Return pixel-center (x, y) of a given cell."""
    x = BOARD_LEFT + col * CELL_SIZE + CELL_SIZE // 2
    y = BOARD_TOP + row * CELL_SIZE + CELL_SIZE // 2
    return x, y

def draw_board():
    """Draw the board shell (background + selection strip + empty holes)."""
    # Background
    screen.fill(BG)

    # Selection strip (top)
    sel_rect = pygame.Rect(PADDING, PADDING, BOARD_WIDTH, SELECT_STRIP_HEIGHT)
    pygame.draw.rect(screen, (50, 50, 55), sel_rect, border_radius=10)
    # Column markers in the strip
    for c in range(COLS):
        cx = BOARD_LEFT + c * CELL_SIZE + CELL_SIZE // 2
        cy = PADDING + SELECT_STRIP_HEIGHT // 2
        pygame.draw.circle(screen, WHITE, (cx, cy), 8)

    # Board background rectangle
    board_rect = pygame.Rect(BOARD_LEFT, BOARD_TOP, BOARD_WIDTH, BOARD_HEIGHT)
    pygame.draw.rect(screen, BOARD_BG, board_rect, border_radius=16)

    # Grid holes (empty)
    token_radius = (CELL_SIZE // 2) - TOKEN_MARGIN
    for row in range(ROWS):
        for col in range(COLS):
            cx, cy = cell_center(col, row)
            pygame.draw.circle(screen, GRID_COLOR, (cx, cy), token_radius + GRID_LINE // 2)
            pygame.draw.circle(screen, EMPTY_COLOR, (cx, cy), token_radius)

    pygame.display.flip()

def place_piece(col:int, row:int, color:tuple) -> bool: 
    """ View-only draw: paint a token at (col,row) with the given color (R,G,B).
    Returns True if (col,row) is within bounds and draws; False otherwise.

    No occupancy checks, no gravity, no turn handling. Your model decides validity,
    then calls this function to reflect the change visually. """
    if screen is None:
        return False
    if not (0 <= col < COLS and 0 <= row < ROWS):
        return False

    cx, cy = cell_center(col, row)
    token_radius = (CELL_SIZE // 2) - TOKEN_MARGIN
    pygame.draw.circle(screen, color, (cx, cy), token_radius)
    pygame.draw.circle(screen, WHITE, (cx, cy), token_radius, width=2)
    pygame.display.flip()
    return True

def sel_column(mouse_pos):
    """Map a mouse position to a column index only within the top selection strip.
    Returns None if outside. No game logic here."""
    # checks that the mouse click in the top selection strip
    x, y = mouse_pos
    if not (PADDING <= x <= PADDING + BOARD_WIDTH and PADDING <= y <= PADDING + SELECT_STRIP_HEIGHT):
        return None
    
    # checks column validity
    col = (x - BOARD_LEFT) // CELL_SIZE
    if 0 <= col < COLS:
        return col
    else: 
        return None

def handle_mouse_click(mouse_pos):
    """Minimal handler: we only care for mouse clicks inside the strip 
    and just call sel_col() to check it """
    return sel_column(mouse_pos)


# =========================
# Main (event-driven, blocking wait, No FPS)
# =========================

def main():
    """TODO STUDENTS: You will need to add things here, 
    for user config (before the main loop)
    and for handling all the game logic (within the main loop) """
    global screen

    # TODO STUDENTS: Define some variables before starting pygame such as ...
    # board         # create a COLSxROW matrix full of zeros
    # vs_machine    # bool
    # ..... 
    # do any config needed, user input etc
    # you can ask option such as colors, 2 or 1 players, etc.
    get_config() # currently does nothing
                
    # starting pygame - No need to touch anthing here
    pygame.init()
    pygame.display.set_caption("Connect 4 Basic")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Allow only the minimal set of events
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONDOWN])
    draw_board() # the board is drawn at the start

    running = True
    while running:
        event = pygame.event.wait()  # blocks until an event arrives
        # we only consider 2 events: QUIT (closing the window) and 
        # MOUSEBUTTONDOWN on the top area of the window, for choosing a column
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            col = handle_mouse_click(event.pos) # returns col number or None
            if col is not None: # player has clicked choosing a column

                # TODO STUDENTS:
                # check if the column has space left
                # find the bottommost empty row of this colum
                # update the board state (consider which player)
                # call place_piece() for painting the new piece
                paint_piece_demo(col) # calls place_piece() just here for demo purposes
                # detect if there are 4 aligned -> if game over -> running = False
                # if not over, if vs_machine make machine move, otherwise flip player (1<->2)

                # THESE ARE JUST HINTS, THE ORDER MIGHT BE DIFFERENT
                # BUT DO IT ALL IN A WELL-STRUCTURED WAY
                # DEFINE AND CALL AS MANY FUNCTIONS AS YOU THINK CONVENIENT


    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()