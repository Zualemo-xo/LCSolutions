class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s=set()
        for i in sentence:
            s.add(i)
        if(len(s)==26):
            return(True)
        return(False)
        