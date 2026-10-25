a=int(input())
def s(i,stri):
    if i==0:
        print(stri)
        return
    s(i-1,stri+"0")
    s(i-1,stri+"1")

s(a,"")

