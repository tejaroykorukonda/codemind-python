def isvowel(c):
    return(c=='a' or c=='e' or c=='i' or c=='o' or c=='u')
def longestvowel(s):
    count,res=0,0
    for i in range(len(s)):
        if(isvowel(s[i])):
            count+=1
        else:
            res=max(res,count)
            count=0
    return max(res,count)
    
s=input()
print(longestvowel(s))