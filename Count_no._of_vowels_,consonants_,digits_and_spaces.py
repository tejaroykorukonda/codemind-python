n=input()
c,d,e,f,i=0,0,0,0,0
while i<len(n):
    if(n[i]=='A'or n[i]=='a'or n[i]=='E'or n[i]=='e'or n[i]=='I' or n[i]=='i' or n[i]=='O'or n[i]=='o' or n[i]=='U' or n[i]=='u'):
        c+=1
    elif(n[i]<='9'and n[i]>='0'):
        d+=1
    elif(n[i]==' '):
        e+=1
    else:
        f+=1
    i+=1
print("Vowels: %d"%c)
print("Consonants: %d"%f)
print("Digits: %d"%d)
print("White spaces: %d"%e)