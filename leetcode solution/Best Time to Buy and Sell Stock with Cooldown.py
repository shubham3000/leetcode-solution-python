class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <2:
            return 0
        sell = 0
        buy = -prices[0]    #if we buy the stock then take it as lost price means take it as negative
        prevBuy =0
        prevSell = 0
        for i in range(len(prices)):
            prevBuy = buy              #first buy the stock, before buy we canot sell the stock
            buy = max(buy,prevSell - prices[i])
            prevSell = sell
            sell = max(sell, prevBuy + prices[i])
        
        return sell
		


"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""