class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # m- no of houses , n - no of paint available cost[i]= [paint1cost,paint2cost,...]
        @cache
        def dp(targetleft,prevcolor,position):
            #base
            if(targetleft<0):
                return(float("inf"))
            if(position==m):
                if(targetleft==0):
                    #print("ANS:",prevcolor)
                    return(0)
                else:
                    return(float("inf"))

            tmp=float("inf")
            if(houses[position]!=0): # If house is already painted, do not repaint
                    #print("KCOC:",position,houses[position])
                    if(prevcolor == houses[position] ): # CURR COLOR DOES NOT MATTER IN THIS CASE
                        tmp=min( tmp,dp(targetleft,houses[position],position+1) )
                    else:
                        tmp=min( tmp,dp(targetleft-1,houses[position],position+1) )
                        
            else:            
                for color in range(1,n+1):
                    #print("TARGET:",targetleft,"PCOLOR:",prevcolor,"CURRCOLOR:",color,"POS:",position)        
                    if(prevcolor==color):
                        tmp=min( tmp,cost[position][color-1]+dp(targetleft,prevcolor,position+1) )
                    else:
                        tmp=min( tmp,cost[position][color-1]+dp(targetleft-1,color,position+1) )
            #print(tmp)
            return(tmp)
                
            
        
        ans=dp(target,-1,0)
        if(ans==float("inf")):
            return(-1)
        return(ans)