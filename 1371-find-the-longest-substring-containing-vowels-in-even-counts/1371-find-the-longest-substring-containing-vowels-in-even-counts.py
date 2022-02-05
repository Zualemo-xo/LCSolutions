class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 525. Contiguous Array SIMILAR SOLN
        #bitmask of 5 vowels in dict
        vow={'a':0b10000,'e':0b01000,'i':0b00100,'o':0b00010,'u':0b00001}
        # vow=['a','e','i','o','u']
        # bmask=[0b10000,0b01000,0b00100,0b00010,0b00001]
        #print(bmask)
        d=defaultdict(int) #defaultdict of 1st occurence of new bitmasks
        curr=0b00000 #iterates and changes values thru each char of string
        d[curr]=-1 #initialiazation
        maxl=0
        
        for i in range(0,len(s)):
            if(s[i] in vow): #if in vowel,increase count by XORing
                curr=curr^vow[s[i]]
            if(curr not in d): #put into hashmap
                d[curr]=i
            else: #calc if this is the max len substring
                maxl=max(i-d[curr],maxl)
        return(maxl)