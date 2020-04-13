/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution {
    public int singleNumber(int[] nums) {
        
        int res = nums[0]; 
        for (int i = 1; i < nums.length; i++) 
            res = res ^ nums[i]; 
      
        return res; 
    }
}
