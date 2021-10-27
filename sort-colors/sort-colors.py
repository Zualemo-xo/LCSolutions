class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt1,cnt2,cnt3=0,0,0
        for i in (nums):
            if(i==0):
                cnt1+=1
            elif(i==1):
                cnt2+=1
            else:
                cnt3+=1
        #print(cnt1)
        for i in range(0,len(nums)):
            
            if(cnt1>0):
                nums[i]=0    
                cnt1-=1
            elif(cnt2>0):
                nums[i]=1
                cnt2-=1
            else:
                nums[i]=2
                #cnt3+=1