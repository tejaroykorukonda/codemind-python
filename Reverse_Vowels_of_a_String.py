a=input()
l=''
for i in a:
    if i in 'aeiouAEIOU':
        l+=i
n=''
for k in a:
    if k in 'aeiouAEIOU':
        n+= l[-1]
        l= l[:-1]
    else:
        n+=k
print(n)