class Solution:
    def maxResult(self, nums, k):
        #Optimal code ,similar as minw
        n = len(nums)
        score = [0] * n
        score[0] = nums[0]
        queue = collections.deque()
        queue.append(0)
        
        for i in range(1, n):
            # pop the old index
            while queue and queue[0] < i-k:
                queue.popleft()
            score[i] = score[queue[0]] + nums[i]
            # pop the smaller value
            while queue and score[i] >= score[queue[-1]]:
                queue.pop()
            queue.append(i)
        return score[-1]
        