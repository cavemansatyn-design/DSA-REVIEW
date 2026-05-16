#smallest in an array
import sys
a=list(map(int,input().split()))
smallest=int(sys.maxsize)
count=0
def ind_smallest(a,smallest):
    count=0
    for t in a:
        count+=1
    for t in range(0,count):
        if a[t]<smallest:
            smallest=a[t]
    print(smallest,t)
ind_smallest(a,smallest)