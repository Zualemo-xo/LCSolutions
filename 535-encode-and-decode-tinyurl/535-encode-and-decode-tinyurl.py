cnt=0
class Codec:
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        global cnt
        self.d={}
        self.d[cnt]=longUrl
        cnt+=1
        return(cnt-1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        #print(shortUrl)
        return(self.d[shortUrl])
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))