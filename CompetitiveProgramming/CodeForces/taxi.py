def solve():
    n = int(input())

    groups = [int(i) for i in input().split(" ")]

    groups.sort()

    p1 = 0
    p2 = n-1

    count = 0 
    while p1 <= p2:
        room = 0
        while p1 <= p2 and room < 4:
            if groups[p1] + room <= 4:
                room += groups[p1]
                p1 += 1
            elif groups[p2] + room <= 4:
                room += groups[p2]
                p2 -= 1
            else:
                break
        
        count += 1
    
    print(count)

solve()