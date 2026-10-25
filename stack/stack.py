# stack=[]
# def push(a):
#     global stack
#     stack.append(a)

# def pop():
#     global stack
#     if len(stack)==0:
#         return "Stack empty"
#     else:
#         l=stack.pop()
#         return l
# def top():
#     global stack
#     if len(stack)==0:
#         return "Stack empty"
#     else:
#         return stack[-1]
# def size():
#     global stack
#     return len(stack)

class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        return len(self.items)==0
    def pop(self,item):
        if len(self.items)==0:
            return "no pop"
        else:

            x=self.items.pop(item)
            return x
    def top(self):
        if len(self.items)==0:
            return "no pop"
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
t=Stack()

