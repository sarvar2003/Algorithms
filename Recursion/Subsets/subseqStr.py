from typing import List
def subsetStr(p: str, up: str): 
    if up == "":
        print(p)
        return 
    
    char = up[0]

    subsetStr(p+char, up[1:])
    subsetStr(p, up[1:])
    
# subsetStr("", "abc")

def subseqInArr(p: str, up: str) -> List[str]:
    if up == "":
        list1 = []
        list1.append(p)
        return list1

    char = up[0]

    left = subseqInArr(p+char, up[1:])
    right = subseqInArr(p, up[1:])

    for ch in right: left.append(ch)

    return left


# print(subseqInArr('', 'abc')) 

def subsetAscii(p: str, up: str): 
    if up == "":
        print(p)
        return 
    
    char = up[0]

    subsetAscii(p+char, up[1:])
    subsetAscii(p, up[1:])
    subsetAscii(p + str(ord(char)), up[1:])


# subsetAscii("", "abc")

def subseqAsciiInArr(p: str, up: str) -> List[str]:
    if up == "":
        return [p]

    char = up[0]

    first = subseqAsciiInArr(p + char, up[1:])
    second = subseqAsciiInArr(p, up[1:])
    third = subseqAsciiInArr(p + str(ord(char)), up[1:])

    for ch in second:
        if ch not in first: first.append(ch)
    for ch in third: 
        if ch not in first: first.append(ch)

    return first

# print (subseqAsciiInArr("", "abca"))

def subsetLoop(arr: List[int])-> List[int]:
    arr.sort()
    outer = [[]]
    end = 0
    start = 0

    for i in range(len(arr)):
        n = len(outer)
        start = 0

        if i > 0 and arr[i] == arr[i-1]:
            start = end + 1 
        
        end = n - 1

        for j in range(start, n):
            internal= outer[j].copy()
            internal.append(arr[i])
            outer.append(internal)
    return outer

print(subsetLoop([1,2,2,3]))
