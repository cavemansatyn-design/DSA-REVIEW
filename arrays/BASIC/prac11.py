#optimised pairsum by two pointer
a=list(map(int,input().split()))
b=int(input())
c=len(a)-1#right pointerr
d=0#left pointer
while d<c:
    if a[d]+a[c]<b:
        d+=1
    elif a[d]+a[c]>b:
        c-=1
    else:
        print(c,d)
        c-=1
        d+=1

