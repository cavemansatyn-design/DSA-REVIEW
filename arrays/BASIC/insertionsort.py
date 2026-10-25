a=list(map(int,input().split()))
for i in range (1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
             a[j+1]=a[j]
             j-=1
        a[j+1]=key
print(a)



a=list(map(int,input().split()))
for i in range (1,len(a)):
       key=a[i]
       for j in range (i-1,-2,-1):
              if j==-1 or a[j]<=key:
                     a[j+1]=key
                     break
              a[j+1]=a[j]
print(a)





