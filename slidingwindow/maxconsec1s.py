a= list(map(int,input().split()))
b= int(input())
# count0=0
# for t in a:
#     if t==0:
#         count0+=1
# if count0==0 or count0==b or count0<b:
#     print(len(a))

# left0=0
# count1=0
# right0=0
# maxans=0
# flip=a[0]
# for t in range(len(a)):

#trying brute
# counts=0
# for t in a:
#     if a==1:
#         counts+=1
#     else:
#         if b!=0:
#             b-=1
#             counts+=1
        
# print(counts)

# maxa=0
# for t in range(len(a)):
#     count=0
#     for tt in range(t,len(a)):
#         if a[tt]==0:
#             count+=1
#         if count>b:
#             break
#     maxa=max(maxa,tt-t+1)
# print(maxa)
#on2

#optimal try
# maxa=0
# left=0
# zeroes=0
# for t in range(len(a)):
#     if a[t]==0:
#         zeroes+=1

#     while zeroes>b:
#         if a[lefgt]==0:
#             zeroes-=1
#         left+=1
#     maxa=max(maxa,t-left+1)
# print(maxa)

#on+on


#full optimal
maxa=0
left=0
zeroes=0
for t in range(len(a)):
    if a[t]==0:
        zeroes+=1

    if zeroes>b:
        if a[left]==0:
            zeroes-=1
        left+=1
    maxa=max(maxa,t-left+1)
print(maxa)


