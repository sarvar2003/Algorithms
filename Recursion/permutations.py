def strPermutations(p: str, up: str):
    if up == "":
        print(p)
        return

    char = up[0]

    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]

        strPermutations(f + char + s, up[1:])
    
# strPermutations("", "abc")

def strPermutationsInArr(p: str, up: str):
    if up == "":
        temp = []
        temp.append(p)
        return temp
    
    char = up[0]
    ans = []
    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]

        for i in strPermutationsInArr(f+char+s, up[1:]): ans.append(i)

    return ans

# print(strPermutationsInArr("", "abc"))

def strPermutationsCount(p: str, up: str):
    if up == "":
        return 1
    
    char = up[0]
    count = 0
    for i in range(len(p)+1):
        f = p[:i]
        s = p[i:]

        count += strPermutationsCount(f+char+s, up[1:])

    return count

print(strPermutationsCount('', "abcd"))
