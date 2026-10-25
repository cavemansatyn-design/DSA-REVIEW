from collections import deque
lst=deque([])
lst.append(100)
lst.append(300)
lst.appendleft(1)
lst.appendleft(9)
lst.popleft()
print(lst)