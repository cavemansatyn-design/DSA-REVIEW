# a=list(map(int,input().split()))

# for i in range(len(a)-1):
#     min_index=i
#     for j in range(i+1,len(a)):
#         if a[j]<a[min_index]:
#             min_index=j
#     a[min_index],a[i]=a[i],a[min_index]
# print(a)

a=list(map(int,input().split()))
for i in range(len(a)-1):
    max_index=i
    for j in range(i+1,len(a)):
        if a[j]>a[max_index]:
            max_index=j
        a[max_index],a[i]=a[i],a[max_index]
print(a)

