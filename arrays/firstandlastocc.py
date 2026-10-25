a=list(map(int,input().split()))
x=int(input())
ans=[]
l=0
r=len(a)-1
f=-1
la=-1
#first
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        f=mid
        r=mid-1
    elif a[mid]>x:
        r=mid-1
    else:
        l=mid+1
ans.append(f)
#last
l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        la=mid
        l=mid+1
    elif a[mid]<x:
        r=mid+1
    else:
        l=mid-1
ans.append(la)
print(*ans)

