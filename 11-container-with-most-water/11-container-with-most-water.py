class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        front,back,area=0,len(h)-1,0
        while(front<back):
            area=max(area,min(h[front],h[back])*(back-front))
            #we aim to get vertical kattai with max height
            if(h[front]>h[back]):
                back-=1
            else:
                front+=1
        return(area)