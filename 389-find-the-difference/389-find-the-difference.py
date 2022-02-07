class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1,d2=defaultdict(int),defaultdict(int)
        for i in s:
            d1[i]+=1
        for i in t:
            d2[i]+=1
        for i in d2:
            if(i not in d1 or d1[i]!=d2[i]):
                return(i)