def triangle(n):
    if n == 0:
        return 
    
    triangle(n-1)
    print(n*"*")

triangle(15)