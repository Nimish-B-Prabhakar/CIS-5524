def create_chess_board(n):

    # creating a board of nxn rows and columns with initial placement of "." as pieces
    board = [["." for _ in range(n)] for _ in range(n)]

    # keep track if same queen doesn't fall on the sam ecolumn
    colums = set()

    # each corresponding diagonal coordinate of a queen will have the same constant values for i,j
    primary_diagonals = set()  # for tracking i - j values
    secondary_diagonals = set()  # for tracking i + j values

    return board, colums, primary_diagonals, secondary_diagonals


create_chess_board(5)
