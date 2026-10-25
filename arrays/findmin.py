a=list(map(int,input().split()))

l=0
r=len(a)-1


while l<=r:
    mid=(l+r)//2
    if a[mid]>a[r]:
        l=mid+1
        
    else:
        r=mid
print(a[l])
