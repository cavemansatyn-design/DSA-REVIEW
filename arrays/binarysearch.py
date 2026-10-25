a=list(map(int,input().split()))
x=int(input())
# l=0
# r=len(a)-1
# while l<=r:
#     mid=(l+r)//2
#     if x==a[mid]:
#         print(mid)
#         break
#     elif x<a[mid]:
#         r=mid-1
#     else:
#         l=mid+1
low=0
high=len(a)-1
def bs(low,high,x,a):
    if low>high:
        return -1
    mid=(low+high)//2
    if a[mid]==x:
        return mid
    elif a[mid]<x:
        return bs(mid+1,high,x,a)
    else:
        return bs(low,mid-1,x,a)
print(bs(low,high,x,a))
