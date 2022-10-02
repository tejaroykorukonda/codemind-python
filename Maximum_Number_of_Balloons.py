text=input()
bCount=0
aCount=0
lCount=0
oCount=0
nCount=0
for ch in text:
    if ch=="b":
        bCount+=1
    elif ch=="a":
        aCount+=1
    elif ch=="l":
        lCount+=1
    elif ch=="o":
        oCount+=1
    elif ch=="n":
        nCount+=1
print(min(bCount,aCount,lCount//2,oCount//2,nCount))