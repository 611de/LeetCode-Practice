#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)

        def dfs(i):
            visited[i] = True
            for x, v in enumerate(isConnected[i]):
                if v == 1 and visited[x] == False:
                    dfs(x)

        privince = 0
        for i in range(len(visited)):
            if visited[i] == False:
                dfs(i)
                privince += 1

        return privince
 
# @lc code=end

