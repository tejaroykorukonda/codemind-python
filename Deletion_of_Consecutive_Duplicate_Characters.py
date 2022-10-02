t=int(input())
for k in range(t):
    s=input()
    s=list(s)
    d=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            d+=1
    print(d)