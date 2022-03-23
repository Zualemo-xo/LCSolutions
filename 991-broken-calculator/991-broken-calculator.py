class Solution(object):
    def brokenCalc(self, start, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        #work backwards
        cnt=0
        while(target>start):
            if(target%2==0):
                target/=2
            else:
                target+=1
            cnt+=1
            #print(target)
        return(cnt+start-target)