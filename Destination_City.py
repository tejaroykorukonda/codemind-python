t=int(input())
a=[]
for i in range(t):
    l=list(map(str,input().split()))
    x=[i for i in l]
    a.extend(x)
print(a[-1])