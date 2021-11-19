class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x=bin(x)[2:]
        y=bin(y)[2:]
        #print(x,y)
        #print([0]*0)
        x1,y1=[],[]
        if(len(x)<len(y)):
            x1=['0']*(len(y)-len(x))
            x1.append(x)
            y1.append(y)
        #elif(len(x)len(y)):
        else:
            y1=['0']*(len(x)-len(y))
            y1.append(y)
            x1.append(x)
        #print(''.join(x1),''.join(y1))
        x1=''.join(x1)
        y1=''.join(y1)
        cnt=0
        for i in range(0,len(x1)):
            if(x1[i]!=y1[i]):
                cnt+=1
        return(cnt)