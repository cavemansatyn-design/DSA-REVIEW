a=list(map(int,input().split()))
x=int(input())
l=0
r=len(a)-1
flag=0
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        flag=1
    if a[l]<=a[mid]:
        if a[l]<=x<a[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if a[mid]<=x<=a[r]:
            l=mid-1
        else:
            l=mid-1
print(True if flag else False)

#O(n) becasue of edge case [777771777777]