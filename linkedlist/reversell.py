#one is stack method of storing value in a list then putting vlaues in reverse order instead of changing the pointer direction 
#better method will be
temp=self.head
prev=None
front=None
while temp!=None:
    front=temp.next
    temp.next=prev
    prev=temp
    temp=front