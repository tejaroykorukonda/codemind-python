a=int(input())
s=0
b=list(map(int,input().split()))
for i in b:
    if i%2==1:
        s+=i
print(s)