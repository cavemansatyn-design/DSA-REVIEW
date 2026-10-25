a=list(map(int,input().split()))
dif=0
flag=0
for t in range(len(a)):
    if a[t]-a[t-1]>0:
        flag=0
    else:
        flag=1
print(flag)