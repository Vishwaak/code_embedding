class test3{
    int fib(int n)
    {
        if(n <= 1)
            return n;
        return fib(n-1) + fib(n-2);
        
    }
    public void string_rep(String x)
    {
        int count;    
        char string[] = x.toCharArray();  
        for(int i = 0; i <string.length; i++) {  
            count = 1;  
            for(int j = i+1; j <string.length; j++) {  
                if(string[i] == string[j] && string[i] != ' ') {  
                    count++;  
                    string[j] = '0';  
                }  
            }
             if(count > 1 && string[i] != '0')  
                System.out.println(string[i]);  
        }
    }
}