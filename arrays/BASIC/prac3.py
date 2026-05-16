#linear search
n=int(input())
b=list(map(int,input().split()))
def linear_search(b,n):
    for i in range(len(b)):
        if n==b[i]:
            print(i)
linear_search(b,n)
    