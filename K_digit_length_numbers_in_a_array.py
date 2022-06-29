def dig(n):
    if n==0:
        return 1
    c=0
    if n<0:
        n=-1*n
    while n:
        n=n//10
        c+=1
    return c
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
c=0
for i in range(n):
    l.append(dig(a[i]))
for i in range(n):
    if dig(a[i])==m:
        c+=1
print(c)