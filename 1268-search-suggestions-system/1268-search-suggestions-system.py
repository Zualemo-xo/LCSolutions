class TrieNode:
    def __init__(self,char=""):
        self.char=char
        self.children={}
        self.is_end=False
    
#FK THIS QSN
        
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
                #print(letter,node.children)
                if(letter in node.children):
                    node=node.children[letter]
                else:
                    new_node=TrieNode(letter)
                    node.children[letter]=new_node #Create new set of children for lettr
                    node=new_node
            node.is_end=True
            
    
        
        def search(part_word):
            node=self.root
            #print(node.children)
            #print(part_word)
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
            #print(node.children, part_word)
            def suggestion(node,suggest_word):
                #print(suggest_word , node.children)
                #print("wtf",self.count)

                # elif(node.is_end==True): #we dont need this word so just return
                #     #print("hi")
                #     return
                if(node.is_end==True and self.count<3 and suggest_word not in self.ans):
                    #print("ANS:",suggest_word)
                    self.ans.append(suggest_word)
                    #print(suggest_word)
                    self.count+=1
                    #return
                
                for i in range(97,123):
                    #print(chr(i))
                    if(self.count>=3):
                        #print("fbvbgbgb")
                        break
                    #print(node.children)
                    if(chr(i) in node.children):
                        #print(chr(i),suggest_word)
                        suggestion(node.children[chr(i)],suggest_word+chr(i))             
                    #print(self.ans)

                
                return
        
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
            #print(searchWord[0:i+1],len(searchWord))
            search(searchWord[0:i+1])
            print("ANSiteration",i,self.ans)
            #self.ans.sort()
            final_ans.append(self.ans)
            self.ans=[]
            self.count=0 #OPEN EYES AND USE EITHER CNT OR COUNT AS VAR NAME DAMNIT
            
        #print(final_ans)
        return(final_ans)

            