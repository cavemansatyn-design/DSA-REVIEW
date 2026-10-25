letters = [
    "",      # 0
    "",      # 1
    "abc",   # 2
    "def",   # 3
    "ghi",   # 4
    "jkl",   # 5
    "mno",   # 6
    "pqrs",  # 7
    "tuv",   # 8
    "wxyz"   # 9
]
a=input()
b=[]
c=[]
d=[]
for t in a:
    b.append(int(t))
print(b)
for t in b:
    c.append(letters[t])
print(c)
def s(i,temp):
    if i==len(a):
        d.append(temp)
        return
    for j in range (len(c[i])):
        s(i+1,temp+c[i][j])

s(0,"")
print(d)



