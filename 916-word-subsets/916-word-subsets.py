class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        #TC: O(N+M)
        # Store the maximum letter count among words2, to reduce it into a single dict
        reference=defaultdict(int)
        for word in words2:
            temp=defaultdict(int)
            for letter in word:
                temp[letter]+=1
            
            for letter in temp:
                if(letter not in reference):
                    reference[letter]=temp[letter]
                else:
                    reference[letter]=max( reference[letter], temp[letter])
        
        #Verify for words1
        ans=[]
        for word in words1:
            temp=defaultdict(int)
            for letter in word:
                temp[letter]+=1
            isTrue=True
            for letter in reference:
                if(letter not in temp or reference[letter]>temp[letter]):
                    isTrue=False
            if(isTrue):
                ans.append(word)
        return(ans)
                    
            
        
        
        
        