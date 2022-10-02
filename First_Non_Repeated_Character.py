t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    r=[]
    for i in s:
        if s.count(i)==1:
            r.append(i)
    if len(r)>0:
        print(r[0])
    else:
        print('-1')