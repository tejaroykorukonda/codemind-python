a=int(input())
s=0
b=list(map(int,input().split()))
for i in range(a):
    if i%2==0:
        s+=b[i]
print(s)