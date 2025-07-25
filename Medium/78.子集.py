#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def dfs(i):
            res.append(path.copy())
            for x in range(i, n):
                path.append(nums[x])
                dfs(x+1)
                path.pop()
        dfs(0)
        return res




        
# @lc code=end

