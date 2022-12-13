from typing import List

board = [
    [True, True, True],
    [True, True, True],
    [True, True, True],
] 
rows, cols = (3,3)
paths = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def allPaths(p: str, maze: List[List[bool]], row: int, col: int):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        print(p)
        return

    if not maze[row][col]:
        return
    
    maze[row][col] = False

    if row < len(maze) - 1:
        allPaths(p + "D", maze, row + 1 , col)
    
    if col < len(maze[0]) - 1:
        allPaths(p + "R", maze, row, col + 1)
    
    if row > 0:
        allPaths(p + "U", maze, row - 1, col)
    
    if col > 0:
        allPaths(p + "L", maze, row, col - 1)
    
    maze[row][col] = True

# allPaths("", board, 0, 0)

def allPathsPrint(p: str, maze: List[List[bool]], row: int, col: int, paths, steps: int):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        paths[row][col] = steps
        for r in paths:
            print(r)
        
        print(p)
        print()
        return

    if not maze[row][col]:
        return
    
    maze[row][col] = False
    paths[row][col] = steps

    if row < len(maze) - 1:
        allPathsPrint(p + "D", maze, row + 1 , col, paths, steps + 1)
    
    if col < len(maze[0]) - 1:
        allPathsPrint(p + "R", maze, row, col + 1, paths, steps + 1)
    
    if row > 0:
        allPathsPrint(p + "U", maze, row - 1, col, paths, steps + 1)
    
    if col > 0:
        allPathsPrint(p + "L", maze, row, col - 1, paths, steps + 1)
    
    maze[row][col] = True
    paths[row][col] = 0


allPathsPrint("", board, 0, 0, paths, 1)