# a=list(map(int,input().split()))
# x=int(input())
# flag=0
# l=0
# r=len(a)-1
# ans=-1
# while l<=r:
#     mid=(l+r)//2
#     if a[mid]==x:
#         print(mid)
#         exit
#     if a[mid]<=a[r]:
#         if a[mid]<=x<=a[r]:
#             l=mid+1
#         else:
#             r=mid-1
#     else:
#         if a[l]<=x<=a[mid]:
#             r=mid-1
#         else:
#             l=mid+1


a=list(map(int,input().split()))
x=int(input())
l=0
r=len(a)-1
# L              M             R
#[10,11,12,13,1,2,3,4,5,6,7,8,9]
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        print(mid)
        exit
    if a[l]<=a[mid]:
        if a[l]<=x<a[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if a[mid]<=x<=a[r]:
            l=mid+1
        else:
            r=mid-1
    



