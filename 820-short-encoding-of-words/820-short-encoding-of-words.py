class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        self.root=TrieNode()
        self.ans=0
        def insert(word):
            node=self.root
            for letter in word:
                if(letter in node.children):
                    node=node.children[letter]
                else:
                    temp=TrieNode()
                    node.children[letter]=temp # Adding new <key,val> pair as <letter,adress of new object>
                    node=temp
            node.isEnd=True
            
        def search(node,wordlen):
            if(len(node.children)>0): #if there are children , continue to iterate as even if isend is true, it is just a suffix  
                for letter in node.children:
                    search(node.children[letter],wordlen+1)
            elif(node.isEnd==True): #So that suffixes are not considred, we need if and elif.
                self.ans+=wordlen 
                self.ans+=1 #to add in #
            return
            
        #Main
        #String needs to be reversed for tries toc dilute out the suffixes
        for word in words:
            insert(word[::-1])
        #Traverse through every valid word , ans keeps track of its length and also adds 1 when isEnd is true , to accomodate for #.
        search(self.root,0)
        return(self.ans)
        