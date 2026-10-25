# a=list(map(int,input().split()))
# ans=[]
# def s(i,temp):
#     if i==len(a):
#         ans.append(sum(temp))
#         return
#     temp.append(a[i])
#     s(i+1,temp)
#     temp.pop()
#     s(i+1,temp)
# s(0,[])
# print(ans)
# a=list(map(int,input().split()))
# ans=[]
# def s(i,temp,suma):
#     if i==len(a):
#         ans.append(suma)
#         return
#     temp.append(a[i])
#     suma+=a[i]
#     s(i+1,temp,suma)

#     f=temp.pop()
#     suma-=f
#     s(i+1,temp,suma)
# s(0,[],0)
# print(ans)

a=list(map(int,input().split()))
ans=[]
def s(i,suma):
    if i==len(a):
        ans.append(suma)
        return
    s(i+1,suma+a[i])
    s(i+1,suma)
s(0,0)
print(ans)