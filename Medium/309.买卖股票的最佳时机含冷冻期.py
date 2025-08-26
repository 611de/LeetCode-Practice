#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            if i<0:
                return 0 if not hold else -inf
            if hold:
                return max(dfs(i-1, hold), dfs(i-2, not hold)- prices[i])
            return max(dfs(i-1, hold), dfs(i-1, not hold) + prices[i])
        return dfs(n-1, False) 
# @lc code=end

