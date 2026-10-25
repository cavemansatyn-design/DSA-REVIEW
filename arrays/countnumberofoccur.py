a=list(map(int,input().split()))
x=int(input())
f=-1
la=-1
l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        f=mid
        r=mid-1
    elif a[mid]<x:
        l=mid+1
    else:
        r=mid-1
l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        la=mid
        l=mid+1
    elif a[mid]<x:
        l=mid+1
    else:
        r=mid-1  
if la==-1 and f==-1:
    print("no")
else:
    print(la-f+1)