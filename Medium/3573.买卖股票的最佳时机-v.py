#
# @lc app=leetcode.cn id=3573 lang=python3
#
# [3573] 买卖股票的最佳时机 V
#

# @lc code=start
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        @cache
        def dfs(i, j, status):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if status else 0
            if status == 0:
                return max(
                    dfs(i - 1, j, 0),
                    dfs(i - 1, j, 1) + prices[i],
                    dfs(i - 1, j, 2) - prices[i],
                )
            if status == 1:
                return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - prices[i])
            return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + prices[i])
        return dfs(n - 1, k, 0)
 
# @lc code=end

