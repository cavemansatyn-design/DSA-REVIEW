a=list(map(int,input().split()))
n=int(input())
k=int(input())
ans=[]
def s(i,n,k,temp):
    if n==0 and k==0:
        ans.append(temp.copy())
        return
    if i==len(a):
        return
    temp.append(a[i])
    s(i+1,n-a[i],k-1,temp)
    temp.pop()
    s(i+1,n,k,temp)
s(0,n,k,[])
print(ans)
        
    