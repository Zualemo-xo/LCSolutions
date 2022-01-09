class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direc='N' #It moves in north/y axis in the start
        N=['W','E'] #LEFT NA GOES WEST,RIGHT EAST
        S=['E','W']
        W=['S','N']
        E=['N','S']
        coord=[0,0]
        for i in instructions:
            #print(coord)
            #print(direc)
            if(direc=='N' and i=='G'):
                coord[1]+=1
            elif(direc=='S' and i=='G'):
                coord[1]-=1
                
            elif(direc=='E' and i=='G'):
                coord[0]+=1
            elif(direc=='W' and i=='G'):
                coord[0]-=1
                
                
            if(direc=='N'):
                if(i=='L'):
                    direc=N[0]
                elif(i=='R'):
                    direc=N[1]
            
            elif(direc=='S'):
                if(i=='L'):
                    direc=S[0]
                elif(i=='R'):
                    direc=S[1]
                    
            elif(direc=='W'):
                if(i=='L'):
                    direc=W[0]
                elif(i=='R'):
                    direc=W[1]
                    
            elif(direc=='E'):
                if(i=='L'):
                    direc=E[0]
                elif(i=='R'):
                    direc=E[1]
        #print("FIN:",coord,direc)
        if(coord[0]==0 and coord[1]==0):
            return(True)
        if(direc=='N'):
            return(False)
        return(True) #all other cases it IT'LL FORM A LOOP IF NOT AT ORIGIN ALSO
                
                
        