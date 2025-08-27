#
# @lc app=leetcode.cn id=1971 lang=python3
#
# [1971] 寻找图中是否存在路径
#

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
               
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = [False]*n

        def dfs(i):
            visited[i] = True
            for x in graph[i]:
                if not visited[x]:
                    dfs(x)
    
        dfs(source)

        return visited[destination] 
# @lc code=end

