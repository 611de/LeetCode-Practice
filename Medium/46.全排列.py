#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = [0]*len(nums)
        def dfs(i, s):
            if i==len(nums):
                res.append(path.copy()) 
            else:
                for x in s:
                    path[i] = x
                    dfs(i+1, s-{x})
        dfs(0, set(nums))
        return res
# @lc code=end

