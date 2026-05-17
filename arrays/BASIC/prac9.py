a=list(map(int,input().split()))
currsum=0
maxsum=-99999999
arr=[]
temp=[]
for t in a:
    currsum+=t
    temp.append(t)
    if currsum>maxsum:
        maxsum=currsum
        arr=temp[:]
    if currsum<0:
        currsum=0
        temp=[]
print(maxsum,arr)
