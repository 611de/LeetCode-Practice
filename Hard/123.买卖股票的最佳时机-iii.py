#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, j, hold):
            if i<0:
                return -inf if hold else 0
            if j<0:
                return -inf
            if hold:
                return max(dfs(i-1, j, hold), dfs(i-1, j, not hold)-prices[i])
            return max(dfs(i-1, j, hold), dfs(i-1, j-1, not hold)+prices[i])
        return dfs(n-1, 2, False) 
# @lc code=end

