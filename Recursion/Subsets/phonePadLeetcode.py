from typing import List

def letterCombinations(digits: str) -> List[str]:
    ans = []
    pad = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    return solve("", digits, ans, pad)
    
def solve(p: str, up: str, ans: List, pad: dict) -> List[str]:
    if up == "":
        ans.append(p)
        return
    
    digit = int(up[0])

    for char in pad[digit]:
        solve(p+char, up[1:], ans, pad)
    
    return ans

print(letterCombinations("24"))