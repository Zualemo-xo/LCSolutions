class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        answer = []
        for num in nums:
            d[num]+=1
        threshold = len(nums)//3

        for num in d:
            if(d[num] > threshold):
                answer.append(num)
        return(answer)
        