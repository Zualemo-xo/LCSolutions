class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters=characters
        self.combinationLength=combinationLength
        self.comb=list(combinations(list(characters),combinationLength ))
        #print(self.comb)
        self.index=0
    def next(self):
        """
        :rtype: str
        """
        i=self.index
        self.index+=1
        return(''.join(self.comb[i]))

    def hasNext(self):
        """
        :rtype: bool
        """
        
        if(self.index==len(self.comb)):
            return(False)
        return(True)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()