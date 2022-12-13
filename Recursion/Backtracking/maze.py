from typing import List

def countWays(row: int, col: int) ->int:
    if row == 1 or col == 1:
        return 1
    
    left = countWays(row - 1, col)
    right = countWays(row, col - 1)

    return left + right

# print(countWays(3,3))

def path(p: str, row: int, col: int):
    if row == 1 and col == 1:
        print(p)
        return

    if row > 1:
        path(p + "D", row - 1, col)
    if col > 1:
        path(p + "R", row, col - 1)


# path("",3,3)

def pathRet(p: str, row: int, col: int) -> List[str]:
    if row == 1 and col == 1:
        temp = [p]
        return temp
    
    ans = []

    if row > 1:
        for path in pathRet(p + "D", row - 1, col):
            ans.append(path)
    if col > 1:
        for path in pathRet(p + "R", row, col-1):
            ans.append(path)    
    
    return ans

# print(pathRet("", 3, 3))

def pathDioganalRet(p: str, row: int, col: int) -> List[str]:
    if row == 1 and col == 1:
        temp = [p]
        return temp
    
    ans = []

    if row > 1:
        for path in pathDioganalRet(p + "V", row - 1, col):
            ans.append(path)
    if col > 1:
        for path in pathDioganalRet(p + "H", row, col-1):
            ans.append(path)    
    if col > 1 and row > 1:
        for path in pathDioganalRet(p + "D", row-1, col-1):
            ans.append(path) 

    return ans

# print(pathDioganalRet("", 3, 3))

def pathRestrictions(p: str, maze: List[List[bool]], row: int, col: int):
    if row == len(maze) - 1 and col == len(maze[0]) - 1:
        print(p)
        return
    
    if not maze[row][col]:
        return

    if row < len(maze) - 1:
        pathRestrictions(p + "D", maze, row + 1, col)
    
    if col < len(maze[0]) - 1:
        pathRestrictions(p + "R", maze, row, col + 1)
    


# pathRestrictions("", board, 0, 0)

