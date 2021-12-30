class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        num="1"
        #mod=-1
        cnt=1
        if(k%2==0 or k%5==0):
            return(-1)

        else:
            while(num!='0'):
                #print("n:",num)
                if(int(num)<k):
                    num+="1"
                    cnt+=1
                else:
                    num=str(int(num)%k)
        return(cnt)
                    