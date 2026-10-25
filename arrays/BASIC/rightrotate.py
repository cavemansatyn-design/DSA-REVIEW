a=list(map(int,input().split()))
k=int(input())
# b=a[-k:]
# a=a[:-k+1]
# print(*(b+a))

def reverse(a,l,r):
    while l<r:
        a[l],a[r]=a[r],a[l]
        l==1
        r-=1
reverse(a,len(a)-k,len(a)-1)
reverse(0,len(a)-k-1)
reverse(0,len(a)-1)


