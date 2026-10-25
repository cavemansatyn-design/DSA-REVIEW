# a=list(map(int,input().split()))
# l=len(a)
# ans=[]
# def subseq(i,temp):
#     if i==l:
#         print(temp)
#         return
#     temp.append(a[i])
#     subseq(i+1,temp)
#     temp.pop()
#     subseq(i+1,temp)
# subseq(0,[])

a=list(map(int,input().split()))
l=len(a)
def s(i,temp):
    if i==l:
        print(temp)
        return
    temp.append(a[i])
    s(i+1,temp)
    temp.pop()
    s(i+1,temp)
s(0,[])