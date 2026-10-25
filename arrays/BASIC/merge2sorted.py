a=list(map(int,input().split()))
b=list(map(int,input().split()))
temp=[]
n=len(a)
m=len(b)
i=0
j=0
# for t in range(min(len(a),len(b))):
#     if a[i]<=a[j]:
#         if a[i] not in temp:
#             temp.append(a[i])
#             i+=1
#         else:
#             i+=1
#     else:
#         if a[j] not in temp:
#             temp.append(a[j])
#             j+=1
#         else:
#             j+=1

# for tt in range(min(len(a),len(b)),max(len(a),len(b))-1):
#     if a[tt] not in temp:
#         temp.append(a[tt])
# print(temp)
while i<n and j<m:
    if a[i]<b[j]:
        if len(temp)==0 or temp[-1]!=a[i]:
            temp.append(a[i])
        i+=1
    else:
        if len(temp)==0 or temp[-1]!=b[j] :
            temp.append(b[j])
        j+=1
while i<n:
    if len(temp)==0 or temp[-1]!=a[i]:
            temp.append(a[i])
    i+=1
while j<m:
    if len(temp)==0 or temp[-1]!=b[j]:
            temp.append(b[j])
    j+=1
print(temp)


    

