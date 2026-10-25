# a=list(map(int,input().split()))
# b=[]
# c=int(input())
# for t in range(len(a)):
#     for tt in range(t,len(a)):
#         if a[t]!=a[tt]:
#             if a[t]+a[tt]==c:
#                 b.append(t)
#                 b.append(tt)
#                 break


# print(b)


a=list(map(int,input().split()))
aa=[]
b={}
c=int(input())
for t in range (len(a)):
    
    req=c-a[t]
    if req in b:
        aa.append(b[req])
        aa.append(t)
        break
    b[a[t]]=t
print(aa)



