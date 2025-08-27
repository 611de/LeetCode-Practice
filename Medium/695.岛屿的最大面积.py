#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        def dfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] != 1:
                return 0
            grid[i][j] = 2
            area = 1
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                area += dfs(x, y)
            return area

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ares = dfs(i, j)
                    res = max(ares, res)
        return res
 
# @lc code=end

