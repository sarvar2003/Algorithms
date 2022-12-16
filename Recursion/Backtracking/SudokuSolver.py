from typing import List

def sudoku(board: List[List[int]]) -> bool:
    row = -1
    col = -1
    n = len(board)

    emptyLeft = False
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: # there is an empty place
                row = i
                col = j
                emptyLeft = True
        
        # if there is an empty place break
        if emptyLeft:
            break
    
    # if there is NO empty place then sudoku is solved
    if not emptyLeft:
        return True
    
    # backtracking to place numbers
    for number in range(1, 10):
        if isSafe(board, row, col, number):
            board[row][col] = number
            if sudoku(board):
                return True
            # backtrack
            board[row][col] = 0

    # if func comes this far it means there is no valid solution for sudoku
    return False

def isSafe(board: List[List[int]], row: int, col: int, number: int) ->  bool:
    # check row
    for i in range(len(board)):
        if board[row][i] == number:
            return False
    
    # check col
    for r in board:
        if r[col] == number:
            return False
        
    # check 3x3 matrix
    rowStart = row - row % 3
    colStart = col - col % 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if board[r][c] == number:
                return False
    
    # check dioganal
    r = 0
    c = 0
    while r < len(board) and c < len(board):
        if board[r][c] == number:
            return False
        r += 1
        c += 1
        

    # [row][col] is safe to place the number
    return True

def display(board: List[List[int]]):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

solved = sudoku(board)

if solved:
    display(board)
else:
    print("Cannot solve")