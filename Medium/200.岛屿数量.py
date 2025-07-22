#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid[0])
        n = len(grid)
        res = 0
        def DFS(grid, i, j):
            
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]!='1':
                return
            grid[i][j] = '2'  
            DFS(grid, i-1, j)
            DFS(grid, i+1, j)
            DFS(grid, i, j+1)
            DFS(grid, i, j-1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res+=1
                    DFS(grid, i, j)
        return res
# @lc code=end

