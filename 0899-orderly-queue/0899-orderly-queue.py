class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t=list(s)
        lt=[]
        if(k>1):
            return(''.join(sorted(t)))
        elif(k==1):
            for i in range(0,len(t)):
                t.append(t.pop(0))
                lt.append(''.join(t))
                #lt.append(''.join(t[1:])+''.join(t[0]))
        #print(lt)        
        lt.sort()
        #print(lt)
        return(lt[0])