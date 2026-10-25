from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        return self.queue.popleft()

    def front(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0