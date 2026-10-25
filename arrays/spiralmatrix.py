a=matrix = [
    [ 1,  2,  3,  4,  5,  6],
    [20, 21, 22, 23, 24,  7],
    [19, 32, 33, 34, 25,  8],
    [18, 31, 36, 35, 26,  9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]
]
#left
for _ in range (len(a)//2):
    d=[]
    b=a.pop(0)
    print(b)
    #down
    for t in range (len(a)):
        print(a[t][-1])
        a[t].pop()
    c=a.pop(-1)
    print(c[::-1])
    for t in range (len(a)):
        d.append(a[t].pop(0))
    print(d[::-1])





        
