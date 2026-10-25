a=list(map(int,input().split()))
b=list(map(int,input().split()))
def unique(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    print(c)
unique(a,b)