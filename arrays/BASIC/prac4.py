#reverse the array using two pointer opr basically inplace swap 
a=list(map(int,input().split()))
def reverse(c):
    l=len(c)
    for i in range((l//2)+1):
        c[i],c[(l-1)-i]=c[(l-1)-i],c[i]
    print(c)
reverse(a)
