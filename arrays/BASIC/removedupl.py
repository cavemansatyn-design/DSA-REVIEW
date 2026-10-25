a=list(map(int,input().split()))
# a=set(a)
# a=list(a)
# a.sort()
# print(a)

# dict={}
# for t in a:
#     dict[t]=0
# print(*dict)

i=0
j=1
count=0
if len(a)==1:
    print(1)
    exit()
for t in range(len(a)-1):
    if a[i]==a[j]:
        j+=1
    elif a[i]!=a[j]:
        a[i+1],a[j]=a[j],a[i+1]
        i+=1
        j+=1
        count+=1
print(i+1)

    

