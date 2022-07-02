/*
#By: Ahmed Moustafa (a.k.a geekahmed)
#Email: geekahmed1@gmail.com
#linkedIn: https://www.linkedin.com/in/geekahmed
#*/

class Solution {
    public int getSum(int a, int b) {
        int uncommonBitsFromBoth = a ^ b;
        int commonBitsFromBoth   = a & b;
    
        if (commonBitsFromBoth == 0)
            return uncommonBitsFromBoth;
        
        return getSum (uncommonBitsFromBoth,  commonBitsFromBoth << 1 );
        
    }
}
