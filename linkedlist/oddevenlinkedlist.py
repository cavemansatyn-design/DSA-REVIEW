# count=1
# dicta={"odd":[],"even":[]}
# a=self.head
# while a is not None:
#     if count%2==1:
#         dicta["odd"].append(a.value)
#     else:
#         dicta["even"].append(a.value)
#     a=a.next
# count=1
# a=self.head

# while dicta["odd"]:
#      a.value=dicta["odd"].pop(0)
#      a=a.next
# while dicta["even"]:
#      a.value=dicta["even"].pop(0)
#      a=a.next

#optimal
#change links

a=self.head
b=a.next
start=b
while a and b is not None:
    a.next=a.next.next
    a=a.next
    b.next=b.next.next
    b=b.next
a.next=b







