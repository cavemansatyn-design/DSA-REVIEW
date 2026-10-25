a=list(map(int,input().split()))
def sum_prod(c):
    sum=0
    prod=1
    l=len(c)
    for i in a:
        sum+=i
        prod*=i
        
    print(sum,prod)
sum_prod(a)