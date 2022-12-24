T = int(input())

for test in range(T):
    X,Y,K = [int(i) for i in input().split(" ")]
    
    distnace = abs(X-Y)
    steps = 1

    while K < distnace:
        distnace -= K
        steps += 1
    
    if X == Y:
        steps = 0
    
    print(steps)