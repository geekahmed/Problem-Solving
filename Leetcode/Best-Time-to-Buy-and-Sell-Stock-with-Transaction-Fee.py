/*
By: Ahmed Moustafa (a.k.a geekahmed)
Email: geekahmed1@gmail.com
linkedIn: https://www.linkedin.com/in/geekahmed
*/

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        sold, hold = 0, -prices[0]
        
        for i in range(1, len(prices)):
            
            sold = max(sold, hold + prices[i] - fee)
            hold = max(hold, sold - prices[i])
        
        return sold
