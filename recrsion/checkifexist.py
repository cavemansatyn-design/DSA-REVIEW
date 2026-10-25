a=list(map(int,input().split()))
k=int(input())
flag=0
result=[]
def s(i,total,arr):
    if i==len(a):
        return False
    if total>k:
        return False
    if total==k:
        result.append(arr.copy())
        return True

    arr.append(a[i])
    total=total+a[i]
    p=s(i+1,total,arr)
    if p==True:
        return True
    else:
        
        t=arr.pop()
        total=total-t
        return s(i+1,total,arr)

if (s(0,0,[])):
    print("Yes")
else:
    print("Flse")


