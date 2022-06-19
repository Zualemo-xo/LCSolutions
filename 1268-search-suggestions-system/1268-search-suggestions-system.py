class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
        
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        self.root=TrieNode()
        def insert(word):
            node=self.root
            for letter in word:
                if(letter in node.children):
                    node=node.children[letter]
                else:
                    new_node=TrieNode()
                    node.children[letter]=new_node #Create new set of children for lettr
                    node=new_node
            node.is_end=True
            
        def suggestion(node,suggest_word):
            if(node.is_end==True and self.count<3 and suggest_word not in self.ans):
                self.ans.append(suggest_word)
                self.count+=1
                #return #We shd not RETURN AND CONTINUE ITERATING TO FIND OTHER LRX SMALL WORDS IN ITS CHILDREN
                
            for i in range(97,123):
                if(self.count>=3):
                    break
                if(chr(i) in node.children):
                    #RECURSIVELY search till this lex smallest word ends
                    suggestion(node.children[chr(i)],suggest_word+chr(i))    
            return
        
        def search(part_word):
            node=self.root
            #traverse till last char in word
            for letter in part_word:
                #print(letter)
                if(letter in node.children):
                    node=node.children[letter]
                else:
                    self.ans=[] #THE TO-BE-SEARCHED STRING IS NOT PRESENT
                    return("False")
                    
            #see what are the possible traversals after this
            #or letter in node.children:
            #CALL A FN TO SEE WHAT WORDS CAN BE FORMED from current 'node'
            suggestion(node,part_word)
            return

        #Main
        #Insert all words into a trie
        for word in products:
            insert(word)
        #For each letter initiate a search like :'h' , 'he' , 'hel', 'hell' 
        final_ans=[]
        self.ans=[]
        self.count=0
        for i in range(0,len(searchWord)):
            search(searchWord[0:i+1])
            final_ans.append(self.ans)
            self.ans=[]
            self.count=0 #OPEN EYES AND USE EITHER CNT OR COUNT AS VAR NAME 

        return(final_ans)

            