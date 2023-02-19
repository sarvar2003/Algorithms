#User function Template for python3
class Solution:
    def maxHeight(self,height, width, length):
        n = len(height)
        rot = [[0,0,0,0] for _ in range(n*3)]
        index = 0
        
        for i in range(n):
            # Copy original box
            rot[index][0] = height[i]
            rot[index][1] = max(width[i], length[i])
            rot[index][2] = min(width[i], length[i])
            rot[index][3] = rot[index][1]*rot[index][2]
            index += 1
            
            # First rotation of the box
            rot[index][0] = width[i]
            rot[index][1] = max(height[i], length[i])
            rot[index][2] = min(height[i], length[i])
            rot[index][3] = rot[index][1]*rot[index][2]
            index += 1
        
            # Second rotation of the box
            rot[index][0] = length[i]
            rot[index][1] = max(width[i], height[i])
            rot[index][2] = min(height[i], width[i])
            rot[index][3] = rot[index][1]*rot[index][2]
            index += 1
        
        
        n *= 3
        
        rot.sort(reverse=True, key=lambda x:x[3])
        
        msh = [0] * n
        
        for i in range(n):
            msh[i] = rot[i][0]
            
        for i in range(1, n):
            for j in range(i):
                if rot[i][1] < rot[j][1] and rot[i][2] < rot[j][2]:
                    if msh[i] < msh[j] + rot[i][0]:
                        msh[i] =  msh[j] + rot[i][0]
        
        return max(msh)
        
t = int(input())

for i in range(t):
    height = [int(i) for i in input().split()]
    width = [int(i) for i in input().split()]
    length = [int(i) for i in input().split()]
    ob = Solution()
    print(ob.maxHeight(height, width, length))
