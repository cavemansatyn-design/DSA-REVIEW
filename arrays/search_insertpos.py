a=list(map(int,input().split()))
x=int(input())
dict={}
for t in range(len(a)):
    dict[a[t]]=t
if x in dict:
    print(dict[x])
if x>a[-1]:
    print("DNE")
if x<a[0]:
    print("DNE")
l=0
r=len(a)-1
ans=0
while l<=r:
    mid=(l+r)//2
    if a[mid]>x:
        ans=mid
        r=mid-1
    else:
        l=mid+1
a.insert(ans,x)
