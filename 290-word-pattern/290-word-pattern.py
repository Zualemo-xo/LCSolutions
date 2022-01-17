class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d=defaultdict(str)
        s=s.split(' ')
        #print(s)
        if(len(s)!=len(pattern)):
            return(False)
        for i in range(0,len(pattern)):
            #print(pattern[i],d[pattern[i]])
            if(d[pattern[i]]==""):
                d[pattern[i]]=s[i]
            elif(d[pattern[i]]!=s[i]):
                return(False)
                #break
            #print(d)
        l=list(d.values())
        if(len(l)!=len(list(set(l)))):
            return(False)
        return(True)