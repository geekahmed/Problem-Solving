/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution {
    public boolean isHappy(int n) {
      
        int slow, fast; 
        slow = fast = n; 
        do{ 
            slow = numSquareSum(slow); 
            fast = numSquareSum(numSquareSum(fast)); 
        }while (slow != fast); 
        return (slow == 1);      
    }
    private int numSquareSum(int n) { 
        int squareSum = 0; 
        while (n!= 0) 
        { 
            squareSum += (n % 10) * (n % 10); 
            n /= 10; 
        } 
        return squareSum; 
} 
}
