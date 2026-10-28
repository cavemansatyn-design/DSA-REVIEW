# a=list(map(int,input().split()))
# t=0
# maxa=0
# len=0
# switch=0
# for tt in range (len(a)):
#     switcher=a[t]
#     if switch==2:
#         break
#     else:
#         len+=1
#         if a[tt]!=switcher:
#             switch+=1
#             switcher=a[tt]
#     t=t+1
#     maxa=max(maxa,len)  
# print(maxa)      


# d={}
# maxa=0
# for t in range(len(a)):
#     len=0
#     if a[t] not in d:
#         if len(d)<=2:
#             d[a[t]]=1
#         else:
#             for tt in d:
#                 len+=d[tt]

#     else:
#         d[a[t]]+=1

#     maxa=max(maxa,len)
# print(d)
# maxa=0
# tttt=[]                
# for t in range(len(a)):
#     ttt=[]
#     for tt in range(t,len(a)):
#         ttt.append(a[tt])
#         tttt.append(ttt.copy())
# print(tttt)

# for t in tttt:
#     lena=0
#     set1=set(t)
#     if len(set1)<=2:
#         lena=len(t)
#     maxa=max(maxa,lena)
# print(maxa)    
#brute one2 and space and time both


a=list(map(int,input().split()))
max_length=0
my_dict={}
left=0
right=0
while right<len(a):
    my_dict[a[right]]=my_dict.get(a[right],0)+1
    if len(my_dict)>2:
        my_dict[a[left]]-=1
        if my_dict[a[left]]==0:
            del my_dict[a[left]]
        left+=1
    if len(my_dict)<=2:
        max_length=max(max_length,right-left+1)
    right+=1
print(max_length)

    