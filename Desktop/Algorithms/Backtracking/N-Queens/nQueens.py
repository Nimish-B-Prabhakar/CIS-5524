def initialize_board(n):
    """
    Initializes an empty N x N board and constraint sets.
    Returns the board and sets for columns, primary diagonals, and secondary diagonals.
    """
    # Create an empty N x N board represented by "."
    board = [["." for _ in range(n)] for _ in range(n)]

    # Initialize sets to keep track of threatened columns and diagonals
    columns = set()
    primary_diagonals = set()  # for tracking i - j values
    secondary_diagonals = set()  # for tracking i + j values

    return board, columns, primary_diagonals, secondary_diagonals


def is_safe(i, j, columns, primary_diagonals, secondary_diagonals):
    """
    Checks if it's safe to place a queen at position (i, j).
    A position is safe if no other queen is in the same column, primary diagonal, or secondary diagonal.
    """
    # Check if the column, primary diagonal, or secondary diagonal is under threat
    if j in columns or (i - j) in primary_diagonals or (i + j) in secondary_diagonals:
        return False  # Position is not safe
    return True  # Position is safe


def place_queens(
    row, n, board, columns, primary_diagonals, secondary_diagonals, solutions
):
    """
    Recursive function to place queens on the board using backtracking.
    If all queens are placed successfully, the current configuration is added to solutions.
    """
    # Base case: if we've placed queens in all rows, we've found a solution
    if row == n:
        # Record the current board configuration as a solution
        solutions.append(["".join(r) for r in board])
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(row, col, columns, primary_diagonals, secondary_diagonals):
            # Place the queen and mark the column and diagonals as occupied
            board[row][col] = "Q"
            columns.add(col)
            primary_diagonals.add(row - col)
            secondary_diagonals.add(row + col)

            # Recurse to place queens in the next row
            place_queens(
                row + 1,
                n,
                board,
                columns,
                primary_diagonals,
                secondary_diagonals,
                solutions,
            )

            # Backtrack: Remove the queen and unmark the column and diagonals
            board[row][col] = "."
            columns.remove(col)
            primary_diagonals.remove(row - col)
            secondary_diagonals.remove(row + col)


def solve_n_queens(n):
    """
    Main function to solve the N-Queens problem.
    Returns all valid solutions where N queens are placed on an N x N board without threatening each other.
    """
    # Step 1: Initialize the board and constraint sets
    board, columns, primary_diagonals, secondary_diagonals = initialize_board(n)

    # Step 2: Prepare a list to collect solutions
    solutions = []

    # Step 3: Start the recursive backtracking algorithm
    place_queens(
        0, n, board, columns, primary_diagonals, secondary_diagonals, solutions
    )

    # Step 4: Return all collected solutions
    return solutions


# Example usage
solutions = solve_n_queens(5)
for solution in solutions:
    for row in solution:
        print(row)
    print()
