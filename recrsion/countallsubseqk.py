a=list(map(int,input().split()))
k=int(input())
# count=0
# def s(i,arr):
#     global count
#     if i==len(a):
#         if sum(arr)==k:
#             count+=1
#         return
        
#     arr.append(a[i])
#     s(i+1,arr)
#     arr.pop()
#     s(i+1,arr)
# s(0,[])
# print(count)
# count=[0]
# def s(i,arr,suma):
#     if i==len(a):
#         if suma==k:
#             count[0]+=1
#         return
#     if suma>k:
#         return 0
    
#     arr.append(a[i])
#     suma=suma+a[i]
#     s(i+1,arr,suma)
#     ll=arr.pop()
#     suma=suma-ll
#     s(i+1,arr,suma)
# s(0,[],0)
# print(count[0])
count=[0]
def s(i,arr,suma):
    if suma==k:
        return 1
    if i==len(a):
        return 0
    
    if suma>k:
        return 0
    
    arr.append(a[i])
    suma=suma+a[i]
    l=s(i+1,arr,suma)
    ll=arr.pop()
    suma=suma-ll
    r=s(i+1,arr,suma)
    return l+r

kk=s(0,[],0)
print(kk)



        