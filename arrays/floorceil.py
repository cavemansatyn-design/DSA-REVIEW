a=list(map(int,input().split()))
x=int(input())
l=0
r=len(a)-1
# L    x      M     x    H
#[1,2,3,4,5,5,5,6,7,8,9,10]
p=[]
low=-1
high=-1
while l<=r:
    mid=(l+r)//2
    if a[mid]>=x:
        low=mid
        r=mid-1
    else:
        l=mid+1

l=0
r=len(a)-1
while l<=r:
    mid=(l+r)//2
    if a[mid]<=x:
        high=mid
        l=mid+1
    else:
        r=mid-1

if high == -1:
    p.append(-1)
else:
    p.append(a[high])

if low == -1:
    p.append(-1)
else:
    p.append(a[low])

print(p)
