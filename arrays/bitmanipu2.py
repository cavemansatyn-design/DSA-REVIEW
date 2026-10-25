# a=int(input())
# b=int(input())
# # a=a^b
# # b=a^b
# # a=a^b

# # print(int(a),int(b))
# # c=1<<b
# # if a&c==0:
# #     print(False)
# # else:
# #     print(True)
# # c=1<<b
# # print(a^c)
# # b=a-1
# # print("TRUE" if a&b==0 else "False")
# b=a^b
# count=0
# for t in bin(b):
#     if t=='1':
#         count+=1
# print(count) 
a=list(map(int,input().split()))
t=0
for tt in a:
    t=t^tt
print(t)