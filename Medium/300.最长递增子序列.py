#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    res = max(res, dfs(j))
            return res+1
        return max(dfs(i) for i in range(len(nums))) 
# @lc code=end

