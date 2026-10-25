# a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# final=[]
# for t in range(len(a)):
#     k=[]
#     for tt in range(len(a[t])):
#         k.append(a[tt][t])
#     final.append(k[::-1])
# print(final)

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for t in range(len(a)):
    for tt in range(t+1,len(a[t])):
        a[t][tt],a[tt][t]=a[tt][t],a[t][tt]
for i in range(len(a)):
    a[i].reverse()

print(a)







