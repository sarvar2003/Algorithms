def fibo(n):
    dp = {}

    return solve(n, dp)

def solve(n, dp):
    if n < 2:
        return n

    if n in dp:
        return dp[n]
    
    dp[n] = solve(n-1, dp)+ solve(n-2, dp)

    return dp[n]

print(fibo(120))
