class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        curr = 0
        ans = []
        for num in pref:
            curr = curr ^ num
            ans.append(curr)
            curr = num
        return(ans)

        