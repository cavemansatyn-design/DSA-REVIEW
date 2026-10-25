# a=list(map(int,input().split()))
# x=int(input())
# l=len(a)
# def s(i,temp):
#     if i==l:
#         if sum(temp)==x:
#             print(temp)
#         return
        
    
#     temp.append(a[i])
#     s(i+1,temp)
    
#     temp.pop()
#     s(i+1,temp)
# s(0,[])
    

a=list(map(int,input().split()))
x=int(input())
l=len(a)
def s(i,total,temp):
    if total==x:
        print(temp)
        return
    elif total>x:
        return
    if i==l:
        return
        
    
    temp.append(a[i])
    total=total+a[i]
    s(i+1,total,temp)
    
    e=temp.pop()
    total=total-e
    s(i+1,total,temp)
s(0,0,[])
    