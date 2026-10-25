a=int(input())

def s(i,open,close,stri):

    if i==0:
        print(stri)
        return
    if open<a:
        s(i-1,open+1,close,stri+"(")
    if close<open:
        s(i-1,open,close+1,stri+")")
s(2*a,0,0,"")