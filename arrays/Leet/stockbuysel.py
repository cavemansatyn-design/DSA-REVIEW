a=list(map(int,input().split()))
# maxa=0
# for t in range (len(a)):
#     sum=0

#     for tt in range(t+1,len(a)):
#         sum=tt-t
#         maxa=max(maxa,sum)
# print(maxa)
minp=a[0]
maxa=0
sum=0
for t in range(len(a)):
    minp=min(a[t],minp)
    sum=a[t]-minp
    maxa=max(sum,maxa)
print(maxa)

#edge case of decreasing 

    

