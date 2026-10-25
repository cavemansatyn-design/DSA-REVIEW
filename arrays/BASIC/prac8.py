#max subarray brute force
listo=[]
a=list(map(int,input().split()))
l=len(a)
for t in range(l):
   
    for t1 in range (t,l):
        listo.append(a[t:t1+1])
sum1=0
for t in listo:
    sum1=max(sum1,sum(t))
print(sum1)
