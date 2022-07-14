"""
Coun the number of moves the bishop can do given its initial position

Total squares visited in Top Left move = min(r, c) – 1
Total squares visited in Top Right move = min(r, 9 – c) – 1
Total squares visited in Bottom Left move = 8 – max(r, 9 – c)
Total squares visited in Bottom Right move = 8 – max(r, c)
where, r and c are the coordinates of the current position of the Bishop on the chessboard.
"""

def bishopMoves(row, column):

    # top left squares
    topLeft = min(row, column) - 1

    # bottom right squares
    bottomRight = 8 - max(row, column)

    # top right squares
    topRight = min(row, 9 - column) - 1

    # bottom left squares
    bottomLeft = 8 - max(row, 9 - column)

    # Return total account

    return (topLeft + topRight + bottomRight + bottomLeft)

# Drive code

# Bishop's position
r = 4
c = 4

print(bishopMoves(r, c))

