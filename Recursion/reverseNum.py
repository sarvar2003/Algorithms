def reverseNum(n):
    if n < 10:
        return n
    

    return (n%10)*pow(10, len(str(n))-1) + reverseNum(n//10)

print(reverseNum(256))
