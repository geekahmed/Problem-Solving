/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution {
    public boolean isPalindrome(int x) {
        int nm = x ; 
        if (x < 0){
            return false;
        } else if (x/10 == 0){
            return (true);
        }else {
            ArrayList<Integer> numDigits = new ArrayList<>();
            while (x > 0){
                numDigits.add(x % 10);
                x /= 10;
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < numDigits.size(); i++) {
              int num = numDigits.get(i);
              sb.append(num);
            }
            String result = sb.toString();
            return (result.equals(Integer.toString(nm)));
        }
    }
}
