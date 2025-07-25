#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        def dfs(i):
            if sum(path)==target:
                res.append(path.copy())
                return
            elif sum(path)>target:
                return
            if i==n-1:
                return
            else:
                for x in range(i, n):
                    path.append(candidates[x])
                    dfs(x)
                    path.pop()
        dfs(0)
        return res
# @lc code=end 

