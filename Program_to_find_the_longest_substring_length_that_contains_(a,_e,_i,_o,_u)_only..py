def isVowel(c):
    return(c =='a' or c =='e' or c=='i' or c =='o' or c =='u')
def longestVowel(s):
    count,res=0,0
    for i in range(len(s)):
        if(isVowel(s[i])):
            count+=1
        else:
            res=max(res,count)
            count=0
    return max(res,count)
    
if __name__=='__main__':
    s=input()
    print(longestVowel(s))