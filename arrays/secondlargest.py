#bruteforce
# a=list(map(int,input().split()))
# l=float("-inf")
# for t in a:
#     l=max(l,t)
# a.remove(l)
# l=float("-inf")
# for t in a:
#     l=max(l,t)
# print(l)

#slight optimization for kth largest
# n=int(input())
# a=list(map(int,input().split()))
# l=float("-inf")
# for _ in range(n):
    
#     l=float("-inf")
#     for t in a:
#         l=max(l,t)
#     a.remove(l)
# for t in a:
#         l=max(l,t)
# print(l)

#pure optimization
# n=int(input())
# a=list(map(int,input().split()))
# a.sort()
# print(a[-n])

# a=list(map(int,input().split()))
# flag=0
# largest=float("-inf")
# slargest=float("-inf")
# for t in a:
#     largest=max(largest,t)
# for tt in a:
#     if tt>slargest and tt!=largest:
#         slargest=tt
# print(slargest)

a=list(map(int,input().split()))
l=float("-inf")
sl=float("-inf")
for t in a:
    if t>l:
        sl=l
        l=t
    else:
        if t>sl and t!=l:
            sl=t
print(sl)