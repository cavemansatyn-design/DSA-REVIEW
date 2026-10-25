# myset=set()
# temp=head
# while temp!=None:
#     if temp in myset:
#         return True
#     else:
#         myset.add(temp)
#         temp=temp.next
# return False
#O(n)
#optimizied is  O(logn)
#fast slow pointer approach
fast=head
slow=head
while fast is not None and fast.next is not None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        return True
return False