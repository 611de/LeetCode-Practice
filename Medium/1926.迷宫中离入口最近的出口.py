#
# @lc app=leetcode.cn id=1926 lang=python3
#
# [1926] 迷宫中离入口最近的出口
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze[0])
        n = len(maze)
        step = 0
        q = deque([(entrance[0], entrance[1])])
        while q:
            step+=1
            for _ in range(len(q)):
                i, j = q.popleft()
                maze[i][j] = '+'
                for x, y in ((i+1, j), (i-1, j), (i, j+1),(i, j-1)):
                    if x>=0 and x<n and y>=0 and y<m and maze[x][y]=='.':
                        if x==0 or x==n-1 or y == 0 or y==m-1:
                            return step
                        q.append((x,y))
                        maze[x][y] = "+"
        return -1 
# @lc code=end

