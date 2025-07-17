#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = int(1e9)
        max_profit  = 0
        for price in prices:
            if price < low_price:
                low_price = price
            elif max_profit < price - low_price:
                max_profit = price - low_price
        return max_profit 
        
# @lc code=end

