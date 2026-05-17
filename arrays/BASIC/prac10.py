def pair_sum(arr,tar):
    for t in range(len(arr)):
        for t1 in range(t+1,len(arr)):
            if arr[t]+arr[t1]==tar:
                print(t,t1)
b=list(map(int,input().split()))
c=int(input())
pair_sum(b,c)