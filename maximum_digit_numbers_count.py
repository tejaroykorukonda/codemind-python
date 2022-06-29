def dig(n):
    v=0
    if n<0:
        n=n*-1
    while n!=0:
        n//=10
        v+=1
    return v
n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    c.append(dig(a[i]))
for i in range(n):
    if dig(a[i])==max(c):
        print(a[i],end=' ')