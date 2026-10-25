# s=input()
# a=[]
# dicta={"(":")","{":"}","[":"]"}
# flag=False
# for t in range(len(s)//2):
#     if dicta[s[t]]==s[len(s)-1-t]:
#         flag=True
# print(flag)

s=input()
a=[]
flag=True
dicta={"(":")","{":"}","[":"]"}
if s=="" or s[0] in ")}]":
    print(False)
else:
    for t in s:
        if t=="(" or t=="{" or t=="[":
            a.append(t)
        else:
            if len(a)==0:
                flag=False
                break
            g=a.pop()
            if t!=dicta[g]:
                flag=False
                break
    if len(a)==0:
        flag=False
    print(flag)

