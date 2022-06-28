a=int(input())
s,c=0,0
b=list(map(int,input().split()))
for i in b:
    if i%2==0:
        s+=i
    else:
        c+=i
print(abs(s-c))