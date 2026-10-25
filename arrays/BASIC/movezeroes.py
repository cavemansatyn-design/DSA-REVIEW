a=list(map(int,input().split()))
i=0
j=1
for t in range(len(a)-1):
    if a[i]==0:
        if a[j]!=0:
            a[i],a[j]=a[j],a[i]
            i+=1
            j+=1
        else:
            j+=1
    else:
        i+=1
        if j<=i:
            j=i+1
print(a)