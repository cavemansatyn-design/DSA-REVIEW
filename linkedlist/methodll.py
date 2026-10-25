# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None

# class SinglyLL:
#     def __init__(self):
#         self.head=None
#     def append(self,val):
#         new_node=Node(val)
#         if self.head==None:
#             self.head=new_node
#         else:
#             curr=self.head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=new_node

# # class Node:
# #     def __init__(self,val):
# #         self.val=val
# #         self.next=None
# # class SLL:
# #     def __init__(self):
# #         self.head=None
# #     def append(self,val):
# #         new_node=Node(val)
# #         if self.head==None:
# #             self.head=self.next
# #         else:
# #             curr=self.head
# #             while curr is not None:
# #                 curr=curr.next
# #             curr.next=new_node
    
#     def traversal(self):
#         if self.head is None:
#             print("Empty")
#         else:
#             curr=self.head
#             while curr is not None:
#                 print(curr.val,end="")
#                 curr=curr.next
#             print()
            
# sll=SinglyLL()
# sll.append(10)
# sll.append(11)
# sll.traversal()

        



# class Node:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
# class SLL:
#     def __init__(self):
#         self.head=None
#     def append(self,val):
#         node=Node(val)
#         if self.head==None:
#             self.head=node
#         else:
#             curr=self.head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=node
#     def traversal(self):
#         if self.head is None:
#             print("Empty")
#         else:
#             curr=self.head
#             while curr is not None:
#                 print(curr.val,sep='')
#                 curr=curr.next
#             print()
# a=SLL()
# a.append(1)
# a.append(2)
# a.traversal()



class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,value):
        new_node=Node(value)
        if self.head==None: #if the linked list was empty so simly app the head in front
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
    def traversal(self):
        if self.head==None:
            print("EMPTY")
        else:
            curr=self.head
            while curr!=None:
                print(curr.val,end="")
                curr=curr.next
            print()
    def insert(self,value,pos):
        new_node=Node(value)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current!=None and count<pos:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.ext=current
    def delete(self,vlaue):
        temp=self.head
        if temp.next!=None:
            if temp.value==vlaue:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp!=None:
                    if temp.value==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("NF")





