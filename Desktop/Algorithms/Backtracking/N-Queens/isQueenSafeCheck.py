def is_queen_safe_check(i, j, columns, primary_diagonals, secondary_diagonals):
    """
    Checks if it's safe to place a queen at position (i, j).
    A position is safe if no other queen is in the same column, primary diagonal, or secondary diagonal.
    """

    # if _ in set -- O(1) time check to see if somethings in a set
    if j in columns or (i - j) in primary_diagonals or (i + j) in secondary_diagonals:
        return False
    return True


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
