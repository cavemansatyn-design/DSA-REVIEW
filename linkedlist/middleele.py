# n=0
# temp=self.head
# while temp!=None:
#     temp=temp.next
#     n+=1
# temp=self.head
# for i in range(0,n//2):
#     temp=temp.next
# return temp

#optimised tortoise and hare method

slow=self.head
fast=self.head
while fast!=None and fast.next!=None:
    slow=slow.next
    fast=fast.next.next
return slow