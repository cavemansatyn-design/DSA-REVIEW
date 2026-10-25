# n = int(input())
# count = 0

# a = self.head
# while a is not None:
#     count += 1
#     a = a.next

# # Edge case: remove head
# if n == count:
#     self.head = self.head.next
#     return

# a = self.head

# for _ in range(count - n - 1):
#     a = a.next

# a.next = a.next.next

slow,fast=head
for _ in range (n):
    fast=fast.next

if fast==None:
    return head.next
while fast.next is not None:
    slow=slow.next
    fast=fast.next
slow.next=slow.next.next
