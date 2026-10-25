class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            return True
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items)==0:
            print("no elements")
            return
        else:
            p=self.items.pop(0)
            return p
    def front(self):
        if len(self.items)==0:
            print("no elements")
            return
        else:
            return self.items[0]
    def rear(self):
        if len(self.items)==0:
            print("no elements")
            return
        else:
            return self.items[-1]
    def size(self):
        if len(self.items)==0:
            print("no elements")
            return
        else:
            return len(self.items)

    

