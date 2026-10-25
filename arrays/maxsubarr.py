a=list(map(int,input().split()))

maxa=float('-inf')
# for i in range (len(a)):
#     sum=0
#     for j in range (i,len(a)):
#         sum+=j
#         maxa=max(maxa,sum)
# print(maxa)
sum=0
for k in a:
    sum+=k
    maxa=max(maxa,sum)
    if sum<0:
        sum=0
print(sum)
    