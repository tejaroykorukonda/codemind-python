x = int(input())
l = list(map(int,input().split()))
y = int(input())
c = -1
d = -1
for i in range(x):
    if l[i]==y and c==-1:
        c=i
    if l[i]==y:
        d=i
print(c,d)