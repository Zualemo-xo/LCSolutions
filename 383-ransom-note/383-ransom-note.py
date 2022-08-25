class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d=defaultdict(int)
        for i in magazine:
            d[i]+=1
        for i in ransomNote:
            if(i not in d or d[i]==0):
                return(False)
            else:
                d[i]-=1
        return(True)
        