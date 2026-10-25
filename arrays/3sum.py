#good work
# a=list(map(int,input().split()))
# result=[]
# for t in range (len(a)):
#     for tt in range (t,len(a)):
#         for ttt in range (tt,len(a)):
#             if a[t]+a[tt]+a[ttt]==0 and t!=tt and tt!=ttt and ttt!=t:
#                 k=[]
#                 k.append(a[t])
#                 k.append(a[tt])
#                 k.append(a[ttt])
#                 k.sort()
#                 if k not in result:
#                     result.append(k)
#                 k=[]
# print(result)
d={}
resu=[]
g=[]
for t in a:
    d[t]=1
for t in range(len(a)):
    for tt in range(t,len(a)):
        if -(a[t]+a[tt]) in d:
            g.append(-(a[t]+a[tt]))
            g.append(a[t])
            g.append(a[tt])
        g.sort()
        resu.append(g)
        g=[]

print(resu)
        

