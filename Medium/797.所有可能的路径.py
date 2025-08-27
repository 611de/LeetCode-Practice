#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        res = []
        path = [0]

        def dfs(i):
            if i == n - 1:
                res.append(path.copy())
                return
            for x in graph[i]:
                path.append(x)
                dfs(x)
                path.remove(x)

        dfs(0)
        return res 
# @lc code=end

