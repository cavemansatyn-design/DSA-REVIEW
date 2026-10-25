a=list(map(int,input().split()))
for i in range(len(a)-2,-1,-1):
    is_swap=False
    for j in range(0,i+1):
        if a[j]<a[j+1]:  #for descen change sign
            a[j],a[j+1]=a[j+1],a[j]
            is_swap=True
    if is_swap==False:
        break
        
print(a)

