class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l=[]
        if(len(nums)==3):
            if(nums[0]+nums[1]+nums[2]==0):
                return([nums])
            
        for i in range(0,len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(left<right):
                
                if(nums[i]+nums[left]+nums[right]==0):
                    if(i!=left and i!=right):
                        t=[nums[i],nums[left],nums[right]]

                        if(t not in l):
                            l.append(t)
                    right-=1
                    left+=1
                elif(nums[i]+nums[left]+nums[right]>0):
                    right-=1
                else:
                    left+=1
        #print(l)
        return(l)
                    