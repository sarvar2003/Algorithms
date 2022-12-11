from typing import List

def pad(p: str, up: str, ans: List):
    if up == "":
        ans.append(p)
        return
    digit = int(up[0])


    for i in range((digit-1)*3, digit*3):
        char = chr(ord("a")+i)
        pad(p+char, up[1:], ans)
    
    return ans

print(pad("", "12", []))