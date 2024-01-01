class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        g_cnt = len(g) - 1
        s_cnt = len(s) - 1
        while(True):
            if(g_cnt < 0 or s_cnt < 0):
                break
            elif(g[g_cnt]<=s[s_cnt]):
                ans += 1
                g_cnt -= 1
                s_cnt -= 1
            else:
                g_cnt -= 1
        return(ans)



        