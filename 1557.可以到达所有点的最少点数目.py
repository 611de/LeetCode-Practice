#
# @lc app=leetcode.cn id=1557 lang=python3
#
# [1557] 可以到达所有点的最少点数目
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        in_dep = [0]*(n)
        for l, r in edges:
            graph[l].append(r)
            in_dep[r] +=1
        
        res = [i for i, d in enumerate(in_dep) if d==0]
        return res 
# @lc code=end

