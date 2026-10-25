a=list(map(int,input().split()))
maxa=0
count=0
for t in a:
    if t==1:
        count+=1
        maxa=max(count,maxa)
    else:
        count=0
print(maxa)