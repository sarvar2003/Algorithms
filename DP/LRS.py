# Longest Repating Subsequence

def solve(s: str):
    n = len(s)

    dp = [ ['']*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + s[i-1] 
            else:
                if len(dp[i-1][j]) > len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    
    return (len(dp[n][n]), dp[n][n])

print(solve("AABBC"))
