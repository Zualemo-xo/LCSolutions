class Solution {
    public String addBinary(String a, String b) {
        char carry='0';
        StringBuffer a1=new StringBuffer(a);
        StringBuffer b1=new StringBuffer(b);
        
        if(a1.length()>b1.length())
        {
            b1.reverse();
            int b1l=b1.length();
            int a1l=a1.length();
            for(int i=0;i<a1l-b1l;i++)
                b1.append("0");
            b1.reverse();
            
        }
        else if(a1.length()<b1.length())
        {
            a1.reverse();
            int b1l=b1.length();
            int a1l=a1.length();
            for(int i=0;i<b1l-a1l;i++)
            {a1.append("0");
                System.out.println("Initialv:"+a1);}
            a1.reverse();
        }
        System.out.println("Initial:"+a1);
        System.out.println("Initial:"+b1);
        //String c="";
        for(int i=a1.length()-1;i>=0;i--)
        {
            //if(a1[i]=='1' && b1[i]=='1')
            //System.out.println(a1);
            
            if(a1.charAt(i)=='1' && b1.charAt(i)=='1')
            {
                if(carry=='0')
                {
                a1.replace(i,i+1,"0");
                //c+='0';    
                carry='1';
                }
                else
                {
                a1.replace(i,i+1,"1");
                //c+='1';
                carry='1';  
                }
            }
            
            else if(a1.charAt(i)=='1' && b1.charAt(i)=='0' || a1.charAt(i)=='0' && b1.charAt(i)=='1')
            {
                if(carry=='0')
                {
                a1.replace(i,i+1,"1");
                //c+='1'; 
                }
                else
                {
                a1.replace(i,i+1,"0");
                //c+='0'; 
                carry='1';  
                }
            }
            
            else if(a1.charAt(i)=='0' && b1.charAt(i)=='0')
            {
                if(carry=='0')
                {
                a1.replace(i,i+1,"0");
                    //c+='0'; 
                }
                else
                {
                  a1.replace(i,i+1,"1");
                    //c+='1'; 
                    carry='0';
                }
            }
            
            
        }
        System.out.println("aasw:"+a1);
        if(carry=='1')
            a1.insert(0,"1");
            //c+="1";
        //System.out.println("aasw:"+a1);
        //System.out.println(carry);
        return(a1.toString());
    }
}