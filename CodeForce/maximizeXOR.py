T = int(input())

for test in range(T):
    A = input()
    B = input()
    
    ones = max(A.count('1'), B.count("1"))
    zeros = len(A) - ones
    
    print(ones * "1" + zeros * "0")
    