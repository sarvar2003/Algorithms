def solve():
    n = input()
    arr = [int(i) for i in input().split()]

    for i  in arr:
        if i == 1:
            print("HARD")
            return
    
    print("EASY")

solve()