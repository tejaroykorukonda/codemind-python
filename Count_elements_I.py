n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in set(a):
    if b.count(i):
        c+=1
for j in set(b):
    if a.count(j):
        c+=1
print(c//2)