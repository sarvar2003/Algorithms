T = int(input())
for test in range(T):
    X,Y = [int(i) for i in input().split(" ")]
    
    if X >= Y * 2:
        print("YES")
    else:
        print("NO")


