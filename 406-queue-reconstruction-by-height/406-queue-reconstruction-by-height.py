class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        people.sort(key=lambda (h,k):(-h,k)) # - refers to sort by descending order
        print(people)

        for h,k in people:
            ans.insert(k,[h,k])
        return(ans)