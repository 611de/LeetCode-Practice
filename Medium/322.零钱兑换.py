#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, j):
            if i<0:
                return inf if j else 0
            if j<coins[i]:
                return dfs(i-1, j)
            return min(dfs(i-1, j), dfs(i, j-coins[i])+1)
        ans = dfs(len(coins)-1, amount)
        return ans if ans<inf else -1 
# @lc code=end

