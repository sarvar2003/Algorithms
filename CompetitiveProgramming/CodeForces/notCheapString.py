def solve(abc):
    w = input()
    p = int(input())
    
    val = 0
    for l in w:
        val += abc[l]
    
    print(val)
    


def main():
    abc = "abcdefghijklmnopqrstuvwxyz"
    alp = {}
    
    for i in range(len(abc)):
        alp[abc[i]] = i

    t = int(input())
    for i in range(t):
        solve(alp)
    
main()