from typing import List

n = 3
board  = [[False]*n for i in range(n)]
def queens(board: List[List[bool]], row: int) -> int:
    if row == len(board):
        display(board)
        print()

        return 1

    count = 0

    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = True
            count += queens(board, row + 1)
            board[row][col] = False
        
    return count

def isSafe(board: List[List[bool]], row, col) -> bool:
    # check vertical cells
    for i in range(row):
        if board[i][col]:
            return False

    # check diogonal left
    toLeft = min(row, col) + 1
    for i in range(1, toLeft):
        if board[row-i][col-i]:
            return False

    # check diogonal right
    toRight = min(row, len(board)-col-1) + 1
    for i in range(1, toRight):
        if board[row-i][col+i]:
            return False
        
    return True

def display(board: List[List[bool]]):
    for row in board:
        for cell in row:
            if cell:
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print()
print(queens(board, 0))