a=list(map(int,input().split()))
b=int(input())
tits=[]
def s(i,suma,op):
    if suma==b:
        tits.append(op.copy())
        return
    if i==len(a):
        return
    if suma+a[i]<=b:
        op.append(a[i])
        s(i,suma+a[i],op)
        l=op.pop()
    s(i+1,suma,op)
s(0,0,[])
print(tits)