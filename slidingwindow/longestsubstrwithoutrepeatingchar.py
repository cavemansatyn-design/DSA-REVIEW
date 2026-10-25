a=input()
dict={}
maxa=0
count=0
t=0

for tt in range(len(a)):
    if a[tt] not in dict:
        dict[a[tt]]=tt
    else:
        t=max(t,dict[a[tt]]+1)
        dict[a[tt]]=tt

    count=tt-t+1
    maxa=max(maxa,count)

print(maxa)