T = int(input())

def main():
    a,b,c = [int(i) for i in input().split()]

    if (a+b == c ) or (a+c ==b) or (b+c == a):
        print("YES")
    else:
        print("NO")

for t in range(T):
    main()