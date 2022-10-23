T = int(input())

def tShirtsizes():        

        a, b = [str(size) for size in input().split()]

        asize = a[-1]
        bsize = b[-1]


        if asize != bsize:
            if asize == 'L':
                print('>')
            elif asize == 'M':
                if bsize == 'S':
                    print(">")
                else:
                    print("<")
            else:
                print("<")
        else:
            if asize == "L":
                if len(a) > len(b):
                    print(">")
                elif len(a) < len(b):
                    print("<")
                else:
                    print("=")
            elif asize == "S":
                if len(a) > len(b):
                    print("<")
                elif len(a) < len(b):
                    print(">")
                else:
                    print("=")
            else:
                print("=") 

for test in range(T):     
    tShirtsizes()


