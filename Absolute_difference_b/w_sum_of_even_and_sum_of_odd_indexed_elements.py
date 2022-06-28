a=int(input())
s,c=0,0
b=list(map(int,input().split()))
for i in range(a):
    if i%2==0:
        s+=b[i]
    else:
        c+=b[i]
print(s-c)