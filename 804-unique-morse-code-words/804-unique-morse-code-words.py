class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d=defaultdict(int)
        
        for w in words:
            temp=""
            for letter in w:
                temp+=morse[ ord(letter)-97 ]
            d[temp]+=1
        
        return(len(d))
        