from  typing import List

n = 4
board = [[False]*n for i in range(n)] 

def knight(board: List[List[bool]], row: int, col: int, knights: int):
    if knights == 0:
        display(board)
        print()

        return 

    if col == len(board) and row == len(board) - 1:
        return 

    if col == len(board):
        knight(board, row+1, 0, knights)
        return 

    if isSafe(board, row, col):
        board[row][col] = True
        knight(board, row, col+1, knights - 1)
        board[row][col] = False
    
    knight(board, row, col+1, knights)
    

def isSafe(board: List[List[bool]], row: int, col: int) -> bool:
    if isValid(board, row-2, col-1):
        if board[row-2][col-1]:
            return False
    
    if isValid(board, row-2, col+1):
        if board[row-2][col+1]:
            return False
        
    if isValid(board, row-1, col-2):
        if board[row-1][col-2]:
            return False
        
    if isValid(board, row-1, col+2):
        if board[row-1][col+2]:
            return False
    
    return True

def isValid(board: List[List[bool]], row: int, col: int) -> bool:
    if (row >= 0 and row < len(board)) and (col >= 0 and col < len(board)):
        return True
    
    return False

def display(board: List[List[bool]]):
    for row in board:
        for cell in row:
            if cell:
                print("K", end=" ")
            else:
                print("-", end=" ")
        print()


knight(board, 0, 0, 4)