
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans=[]
        pattern=pattern+"1"
        
        for word in words:
            word=word+"1"
            ispattern=True
            bijection=defaultdict(str)
            bijection1=defaultdict(str)
            
            for pos,letter in enumerate(pattern):
                if(letter in bijection1 and bijection1[letter]!=word[pos]):
                    ispattern=False
                bijection1[ letter ] = word[pos]

                    
            for pos,letter in enumerate(word):
                print(bijection)
                if(letter in bijection and bijection[letter]!=pattern[pos]):
                    ispattern=False
                bijection[ letter ] = pattern[pos]
      
            if(ispattern):
                ans.append(word[:-1])
                
        return(ans)

            
        
        
        