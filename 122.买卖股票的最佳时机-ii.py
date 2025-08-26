#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, hold), dfs(i-1, not hold)-prices[i])
            return max(dfs(i-1, hold), dfs(i-1, not hold)+prices[i])
        
        return dfs(n-1, False)
         
# @lc code=end

