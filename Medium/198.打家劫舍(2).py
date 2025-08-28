#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i<0:
                return 0
            return max(dfs(i-2) + nums[i], dfs(i-1))
        
        return dfs(len(nums)-1)
            
# @lc code=end

