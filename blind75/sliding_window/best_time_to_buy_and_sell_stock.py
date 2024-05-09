# maxProfit2:
# don't need to keep track of indices, just values of l and r
# because we are not playing with indices - we also don't need 
# to do preliminary check if len(prices) > 1

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        buy = prices[0]
        
        for price in prices:
            if price < buy:
                buy = price
            else:
                max_profit = max(price-buy, max_profit)
        
        return max_profit
    
    
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            
            else:
                max_profit = max(prices[r] - prices[l], max_profit)
                
        return max_profit