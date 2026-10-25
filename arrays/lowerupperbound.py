a=list(map(int,input().split()))
x=int(input())
# if x<a[0]:
#     print("no upperbound")
# elif x>a[-1]:
#     print("no lower bound")
# else:
#     l=0
#     r=len(a)-1
#     while l<=r:
#         mid=(l+r)//2
#         if a[mid]>=x:
#             ans=mid
#             r=mid-1
#         else:
#             l=mid+1
# print(ans)
#lowerbound
ans=0
l=0
r=len(a)-1
while l<=r:



    mid=(l+r)//2
#     if a[mid]>=x:
#         ans=mid
#         r=mid-1
#     else:
#         l=mid+1
# L            M               H
# [1,1,2,3,4,5,6,7,,7,7,8,8,9,10]
# [0,1,2,3,4,5,6,7,8,9,10,11,12]
# upper bound for 1 

#uppperbound
    # if a[mid]>x:
    #     ans=mid
    #     l=mid+1
    # else:
    #     r=mid-1
#lowerbound is the smallest index such that the number is greater than equal to the target
#uppperbound is the smallestr index such that the number is greater than the target

# L            M               H
# [1,1,2,3,4,5,6,7,,7,7,8,8,9,10]
# [0,1,2,3,4,5,6,7,8,9,10,11,12]
# lowerbound bound for 1 
#     if a[mid]>=x:
#         ans=mid
#         r=mid-1
#     else:
#         l=mid+1
# print(ans)
#upperbound

    if a[mid]>x:
        ans=mid
        r=mid-1
    else:
        l=mid+1
