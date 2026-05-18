b=int(input())
e=int(input())
ans=1
if e<0:
    b=1/b
while e>0:
    if e%2==1:
        ans=ans*b
    b=b*b
    e=e//2
print(ans)


