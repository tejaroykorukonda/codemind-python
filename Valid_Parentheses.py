def isbalance(s):
    while True:
        if '()' in s:
            s=s.replace('()','')
        elif '[]' in s:
            s=s.replace('[]','')
        elif '{}' in s:
            s=s.replace('{}','')
        else:
            return not s

t=int(input())
for i in range(t):
    s=input()
    if isbalance(s):
        print("True")
    else:
        print("False")