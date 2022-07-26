from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
# customQueue.popleft()
customQueue.append(4)
customQueue.clear()
print(customQueue)