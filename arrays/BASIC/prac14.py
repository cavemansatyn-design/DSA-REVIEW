a=int(input())
b=[]
while a>0:
    b.append(a%10)    
    a=a//10
b.reverse()
print(b)