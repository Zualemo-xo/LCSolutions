class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        cnt=0
        for i in range(0,len(nums)):
            if(nums[i] in d and d[nums[i]]>2):
                #print("f")
                while(d[nums[i]]>2):
                    nums.pop(i)
                    nums.append("")
                    cnt+=1
                    #print(nums)
                    d[nums[i]]-=1
        #print(nums[:len(nums)-cnt])
        for i in range(0,cnt):
            nums.pop()
        
                