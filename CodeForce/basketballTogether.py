N, D = [int(i) for i in input().split(' ')]

P = [int(i) for i in input().split(' ')]
P.sort()

max_wins = 0
while P:
    org = P.pop() # current max power 
    currentPower = org  # total power so far

    while P and currentPower <= D:
        P.pop(0)
        currentPower += org

    if currentPower > D:
        max_wins += 1

print(max_wins)


