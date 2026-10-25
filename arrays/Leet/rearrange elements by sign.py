# a=list(map(int,input().split()))
# arr1=[]
# arr2=[]
# l=len(a)
# for t in a:
#     if t<0:
#         arr1.append(t)
#     else:
#         arr2.append(t)
# dict1={}
# dict1["neg"]=arr1
# dict1["posa"]=arr2
# result=[]
# for kk in range(l):
#     if kk%2==0:
#         result.append(dict1["neg"].pop())
#     else:
#         result.append(dict1["posa"].pop())
# print(result)

a=list(map(int,input().split()))
pi=0
ni=1
result=[0]*(len(a))
for t in a:
    if t>=0:
        result[pi]=t
        pi+=2
    else:
        result[ni]=t
        ni+=2
print(result)