# def binarySearch(nums,target):
#     n=len(nums)
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(high+low)//2
#         if nums[mid]==target:
#             print(mid)
#             return mid or write break print writes and return/break breaks
#         elif nums[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1


def binarySearch(nums,low,high,target):
    n=len(nums)
    low=0
    high=n-1
    if low>high:
        return -1
    mid=(low+high)//2

    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        binarySearch(nums,mid+1,high,target)
    else:
        binarySearch(nums)
