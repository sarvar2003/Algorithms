T = int(input())

def main():
    lenArr = input()
    arr = [int(i) for i in input().split()]

    yes = True

    arr.sort()

    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            yes = False    

    if yes:
        print("YES")
    else:
        print("NO")
    


for t in range(T):
    main()

