a=[[7,9,2,3],[20,9,0,10],[29,0,-10,5],[4,14,6,7]]
# g=[]
# count=0
# for t in range (len(a)):
#     for tt in range (len(a[t])):
#         if a[t][tt]==0:
#             a[t]=[0]*len(a)

#             g.append(tt)
#             break
# g=(set(g))
# for t in range (len(a)):
#     for tt in range (len(a[t])):
#         if tt in g:
#             a[t][tt]=0
# print(a)

col=[0 for _ in range (len(a))]
row=[0 for _ in range (len(a[0]))]

for t in range(len(a)):
    for tt in range(len(a[t])):
        if a[t][tt]==0:
            row[tt]=1
            col[t]=1
matrix=[[0 for _ in range (len(a[0]))]for _ in range (len(a))]
for t in range (len(a)):
    for tt in range (len(a[t])):
        if row[tt]==1 or col[t]==1:
            a[t][tt]=0
print(a)    
