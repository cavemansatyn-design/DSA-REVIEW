a=list(map(int,input().split()))
l=float("-inf")
for t in a:
    l=max(t,l)
print(l)