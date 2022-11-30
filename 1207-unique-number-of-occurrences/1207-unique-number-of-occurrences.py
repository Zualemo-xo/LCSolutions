class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d,s=defaultdict(int),set()
        for i in arr:
            d[i]+=1
        for i in d:
            if(d[i] in s):
                return(False)
            else:
                s.add(d[i])
        return(True)
        