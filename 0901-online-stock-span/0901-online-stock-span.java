class StockSpanner {
    // own java code after a long tym wow
    Stack <ArrayList> s=new Stack();

    public int next(int price) {
        int cnt=1;
        //System.out.println(s);
        if(s.size()==0)
        {
            ArrayList <Integer> l = new ArrayList();
            l.add(price);
            l.add(cnt); //add cnt
            s.push(l);
            //System.out.println( ((s.peek()).get(0)).getClass().getName());
            return(cnt);
        }
        while(s.size()>0 && (int)(s.peek()).get(0)<=price)
        {
            // s.pop();
            cnt+=(int)s.pop().get(1);
            //System.out.println(cnt);
        }
        
        ArrayList <Integer> l = new ArrayList();
        l.add(price);
        l.add(cnt);
        s.push(l);
        return(cnt);
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */