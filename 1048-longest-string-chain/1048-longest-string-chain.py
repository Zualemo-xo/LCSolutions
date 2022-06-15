class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #LIS concept isemms
        prevword_chain=defaultdict(int)
        #Order words array be length of words in ASC
        words.sort(key= lambda x:len(x))
        minlen=len(words[0])
        for i in words:
            if(len(i)==minlen):
                prevword_chain[i]=1
            else:
                maxval=1
                for j in range(0,len(i)):
                    word=i[0:j]+i[j+1:]
                    if(word in prevword_chain):
                        maxval=max(maxval,prevword_chain[word]+1)
                prevword_chain[i]=maxval
        #print(prevword_chain)
        return(max(prevword_chain.values()))