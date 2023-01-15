"""
Time complexity: O(N^2)
Space complexity: O(N*M) 
"""
def solve(s: str, pattern: str) -> bool: 
    n1 = len(s)
    n2 = len(pattern)

    dp = [[""]*(n2+1) for _  in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1] + s[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    
    return dp[n1][n2] == pattern

print(solve("acddafdb", "aab"))


"""
Time complexity : O(N+M)
Space complexity : O(1)
"""
def solve2(s: str, pattern : str) -> bool:
    p1, p2 = 0, 0

    while p1 < len(s) and p2 < len(pattern):
        if s[p1] == pattern[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1
    
    return p2 == len(pattern) 
        


print(solve2("acddafdb", "aab"))
