#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        queue = []
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append((i, j))
                elif grid[i][j]==1:
                    fresh+=1

        res = 0
        while queue and fresh:
            temp_queue = []
            res+=1
            while queue:
                p = queue.pop(0)
                i,j = p
               
                for x,y in ((i+1, j),
                (i-1, j),
                (i, j-1),
                (i, j+1)):
                    if x>=0 and x<n and y>=0 and y<m and grid[x][y]==1:
                        grid[x][y]=2
                        fresh-=1
                        temp_queue.append((x,y))
            queue = temp_queue
        
        return -1 if fresh else res 
# @lc code=end

