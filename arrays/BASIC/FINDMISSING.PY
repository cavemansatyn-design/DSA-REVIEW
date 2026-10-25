# a = list(map(int, input().split()))
# kkk = int(input())

# k = {}

# for t in range(0, kkk + 1):
#     k[t] = 0

# for kk in k:
#     if kk in a:
#         k[kk] += 1

# for tt in k:
#     if k[tt] == 0:
#         print(tt)

a = list(map(int, input().split()))
kkk = int(input())
s=sum(a)
if s==(kkk*(kkk+1))/2:
    if 0 in a:
        print("Y")
else:
    print(s-(kkk*(kkk+1))/2)