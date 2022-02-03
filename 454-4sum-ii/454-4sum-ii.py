class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        l1={}
        cnt=0
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                s=nums1[i]+nums2[j]
                if(l1.has_key(s)):
                    l1[s]=l1.get(s)+1
                else:
                    l1[s]=1
        for i in range(0,len(nums3)):
            for j in range(0,len(nums4)):
                s=-nums3[i]-nums4[j]
                if(l1.has_key(s)):
                    cnt+=l1.get(s)
        return(cnt)