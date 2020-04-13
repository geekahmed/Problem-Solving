/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0 ; i < nums.length ; i++){
            for (int j = i + 1 ; j < nums.length ; j++){
                if (nums[j] == target - nums[i]){
                    return new int[] {i , j} ; 
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
