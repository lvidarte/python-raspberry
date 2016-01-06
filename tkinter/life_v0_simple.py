"""
Las transiciones dependen del número de células vecinas vivas:

  * Una célula muerta con exactamente 3 células vecinas vivas "nace"
    (al turno siguiente estará viva).
  * Una célula viva con 2 ó 3 células vecinas vivas sigue viva,
    en otro caso muere o permanece muerta (por "soledad" o "superpoblación").

"""

# Glider
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

WIDTH  = len(board[0])
HEIGHT = len(board)
DEAD   = 0
ALIVE  = 1


def get_neighbors(cell, board):
    x_center, y_center = cell

    x_left  = x_center-1 if x_center-1 >= 0     else WIDTH-1
    x_right = x_center+1 if x_center+1 < WIDTH  else 0
    y_up    = y_center-1 if y_center-1 >= 0     else HEIGHT-1
    y_down  = y_center+1 if y_center+1 < HEIGHT else 0

    return (board[y_up][x_left],
            board[y_up][x_center],
            board[y_up][x_right],
            board[y_center][x_left],
            board[y_center][x_right],
            board[y_down][x_left],
            board[y_down][x_center],
            board[y_down][x_right])

def get_next_generation(board):
    board_ = [[DEAD] * WIDTH for _ in range(HEIGHT)]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cell = board[y][x]
            neighbords = get_neighbors((x, y), board)
            board_[y][x] = evolve(cell, neighbords)
    return board_

def evolve(cell, neighbords):
    alive_neighbords = neighbords.count(ALIVE)
    if (cell == DEAD and alive_neighbords == 3) or \
       (cell == ALIVE and alive_neighbords in (2, 3)):
        return ALIVE
    else:
        return DEAD

def show(board):
    for row in board:
        print(' '.join([' ' if col == DEAD else '#' for col in row]))

for i in range(8):
    show(board)
    board = get_next_generation(board)
    print("-" * 16)

