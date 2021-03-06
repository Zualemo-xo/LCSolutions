class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #0-1 KNAPSACK MEMOIZATION TC: O(N.M) SC:O(N.M)
        #memo[posS1][PosS2]
        self.memo=[[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        def dp(posS1,posS2):
            posS3=posS1+posS2
            #Memoization
            if(self.memo[posS1][posS2]!=-1):
                return(self.memo[posS1][posS2])
                
            if( posS3==len(s3) ):
                if( posS2==len(s2) and posS1==len(s1) ):
                    #print("rgb")
                    return(True)
                else:
                    return(False)
            else:
                if(posS2>=len(s2)): #    Lerngth idn exceeded
                    if(s1[posS1]==s3[posS3]):
                        x=  dp(posS1+1,posS2)
                    else:
                        x=False
                    
                
                elif( posS1>=len(s1) ):
                    if(s2[posS2]==s3[posS3]):
                        x=  dp(posS1,posS2+1)
                    else:
                        x= False
                    
                
                elif(s2[posS2] != s3[posS3] and s1[posS1] != s3[posS3]):
                    x=False
                else:
                    if(s1[posS1]==s2[posS2] and s2[posS2]==s3[posS3]): #Both strings could take this string
                        x=  dp(posS1,posS2+1) | dp(posS1+1,posS2)
                    elif(s1[posS1]==s3[posS3]):
                        x=  dp(posS1+1,posS2)
                    elif(s2[posS2]==s3[posS3]):
                        x=  dp(posS1,posS2+1)
                    #print(posS1,posS2,posS3,s1[posS1],s2[posS2], s3[posS3])    
                self.memo[posS1][posS2]=x
                return(x)
        
        if(len(s1)+len(s2)!=len(s3)): # Edge
            return(False)
        return(dp(0,0)) #start selecting with S1
        #dp(False,0,0,0)
                    
                