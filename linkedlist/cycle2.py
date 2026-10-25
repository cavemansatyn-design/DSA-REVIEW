# myset=set()
# temp=head
# while temp!=None:
#     if temp in myset:
#         return temp
#     else:
#         myset.add(temp)
#         temp=temp.next
# return False

#slowfastapprocachfloydcycle
slow=head
fast=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
return None