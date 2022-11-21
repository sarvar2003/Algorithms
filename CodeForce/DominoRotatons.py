def solve(tops, bottoms):
    rotations = 0
    for i in range(len(tops)-1):
        if tops[i] == tops[i+1]:
            continue
        else:
            if bottoms[i+1] == tops[i]:
                tops[i+1] = bottoms[i+1]
                rotations += 1
            elif bottoms[i] == tops[i+1]:
                tops[i] = bottoms[i]
                rotations += 1
            else:
                return -1
    
    if len(set(tops)) == 1:
        return rotations
    
    print(tops)
    
    rotations = 0
    for i in range(len(bottoms)-1):
        if bottoms[i] == bottoms[i+1]:
            continue
        else:
            if tops[i+1] == bottoms[i]:
                bottoms[i+1] = tops[i+1]
                rotations += 1
            elif tops[i] == bottoms[i+1]:
                bottoms[i] = tops[i]
                rotations += 1
            # else:
                # return -1
            
    if len(set(bottoms)) == 1:
        return rotations
    print(bottoms)

print(solve([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))