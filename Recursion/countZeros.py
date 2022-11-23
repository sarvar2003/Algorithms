def countZeros(n):
    return helper(n, 0) 

def helper(n, zeros):
    if n < 10 :
        return zeros
    if n % 10 == 0:
        return helper(n//10, zeros+1)
    return helper(n//10, zeros)

def count2(n):
    zeros = 0

    while n >= 10:
        if n % 10 == 0:
            zeros += 1
        
        n = n//10
    
    return zeros

print(countZeros(1205200030))
print(count2(1205200030))