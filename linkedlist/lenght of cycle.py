# myset={}
# temp=head
# count=0
# while temp!=None:
#     count+=1
#     if temp in myset:
#         return count-myset[temp]
#     else:
        
#         myset[temp]=count
#         temp=temp.next
# return 0
    

slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        slow.next
        count=1
        while slow!=fast:
            slow=slow.next
            count+=1
        return count