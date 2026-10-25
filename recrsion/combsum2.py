a=list(map(int,input().split()))
b=int(input())
c=[]
def s(i,l,suma):
    if suma==b:
        temp=sorted(l)
        if temp not in c:
            c.append(l.copy())
        return
    if len(a)==i:
        return
    if suma+a[i]<=b:
        l.append(a[i])
        s(i+1,l,suma+a[i])
        l.pop()

    s(i+1,l,suma)
s(0,[],0)
print(c)

    
# a=list(map(int,input().split()))
# b=int(input())
# c=[]
# def s(i,l,suma):
#     if suma==b:
#         l.sort()
#         c.append(l.copy())
#         return
#     if len(a)==i:
#         return
#     if suma+a[i]<=b:
#         l.append(a[i])
#         s(i+1,l,suma+a[i])
#         l.pop()

#     s(i+1,l,suma)
# s(0,[],0)
# print(c)

    