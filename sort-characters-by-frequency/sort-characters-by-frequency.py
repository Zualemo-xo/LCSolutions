class Solution:
    def frequencySort(self, s: str) -> str:
        ans,x="",collections.Counter(s).most_common()
        for key,value in x:
            ans+=key*value
        return(ans)