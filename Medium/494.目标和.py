#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target+=sum(nums)
        if target<0 or target%2!=0:
            return 0
        p  = target // 2
        @cache
        def dfs(i, c):
            if i<0:
                return 1 if c==0 else 0
            if c < nums[i]:
                return dfs(i-1, c)
            return dfs(i-1, c) + dfs(i-1, c-nums[i])
        
        return dfs(len(nums)-1, p) 
# @lc code=end

