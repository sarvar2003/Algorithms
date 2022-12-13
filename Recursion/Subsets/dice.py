from typing import List

def dice(p: str, target: int):
    if target == 0:
        print(p)
        return
    
    for i in range(1, 7):
        if i <= target:
            dice(p + str(i), target - i)
        else:
            break

def diceRet(p: str, target: int):
    if target == 0:
        temp = [p]
        return temp
    
    ans = []

    for i in range(1, 7):
        if i <= target:
            for c in diceRet(p + str(i), target-i):
                ans.append(c)
        else:
            break
    
    return ans

def diceCustFace(p: str, target: int, face: int):
    if target == 0:
        temp = [p]
        return temp
    
    ans = []

    for i in range(1, face):
        if i <= target:
            for c in diceRet(p + str(i), target-i):
                ans.append(c)
        else:
            break
    
    return ans
    
    
print(diceCustFace("", 8, 8))
