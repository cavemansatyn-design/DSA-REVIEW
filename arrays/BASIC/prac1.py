#smallest in an array
import sys
a=list(map(int,input().split()))
smallest=int(sys.maxsize)
for t in a:
    if t<smallest:
        smallest=t
print(smallest)