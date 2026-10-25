a=list(map(int,input().split()))
# a=sorted(set(a))
# maxac=1
# count=1
# diff=0
# for t in range (1,len(a)):
#     if a[t]-a[t-1]==1:
#         count+=1
        
#     else:
#         maxac=max(maxac,count)
#         count=1
# maxac=max(maxac,count)
# print(maxac)

a=set(a)
dict={}
count=1
l=1
for t in a:
    dict[t]=True

for t in dict:
    if t-1 not in dict:
        count=1
        current=t
    while current+1 in dict:
        count+=1
        current+=1
    l=max(l,count)
print(l)
        

