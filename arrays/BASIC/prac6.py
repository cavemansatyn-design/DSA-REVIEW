a=list(map(int,input().split()))
def unique(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
unique(a)