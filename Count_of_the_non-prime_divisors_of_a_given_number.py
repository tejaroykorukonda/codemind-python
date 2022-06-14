def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
d=len(a)
for j in a:
    if prime(j):
        c+=1
print(d-c)
    