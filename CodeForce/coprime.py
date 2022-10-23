import math
T = int(input())


def main():
    res = []
    lenArr = int(input())

    arr = [int(i) for i in input().split()]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if math.gcd(arr[i], arr[j]) == 1:
                res.append(i+j + 2) 
    
    if len(res) == 0:
        print(-1)
        return 

    # print(res)
    print(max(res))

for t in range(T):
    main()

