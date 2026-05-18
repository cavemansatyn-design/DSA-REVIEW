flag=0
a=list(map(int,input().split()))
r=len(a)-1
l=0
while l<r:
    if a[l]==a[r]:
        l=l+1
        r=r-1
    else:
        flag=1
        break
if flag==0:
    print("yes")
else:
    print("no")