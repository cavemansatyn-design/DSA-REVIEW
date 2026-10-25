arr=[[1,2],[4,5],[7,8]]
#num of rows=len(arr)
#num of columns=len(arr[0])
# for t in arr:
#     for tt in t:
#         print(tt,end='')
#     print("")
# for tt in range(len(arr)):
#     for t in arr:
#         print(t[tt])
# for t in range(len(arr)):
#     for tt in range(len(arr[0])):
#         if t>=tt:
#             print(arr[t][tt],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# 1 2 
# 4 5 
# 7 8 
# 1 4 7
# 2 5 8
row=len(arr)
col=len(arr[0])
arrt=[[0]*row for _ in range(col)]
for k in range(len(arrt)):
    for kk in range(len(arrt[k])):
        arrt[k][kk]=arr[kk][k]
print(arrt)

