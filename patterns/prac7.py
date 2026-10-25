a=1
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(a,end="")
        a+=1

    print()