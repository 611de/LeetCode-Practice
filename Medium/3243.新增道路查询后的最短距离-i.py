#
# @lc app=leetcode.cn id=3243 lang=python3
#
# [3243] 新增道路查询后的最短距离 I
#

# @lc code=start
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[i+1] for i in range(n-1)]
        # dis = [-1]*n

        def bsf(i):
            dis = [-1]*n
            step = 0
            cur = [0]
            while cur:
                step+=1
                nxt = []
                for node in cur:
                    for x in graph[node]:
                        if x == n-1:
                            return step
                        if dis[x] != 1:
                            dis[x] = 1
                            nxt.append(x)
                cur = nxt
        
        ans = []
        for i, (l,r) in enumerate(queries):
            graph[l].append(r)
            ans.append(bsf(i))
        return ans 
# @lc code=end

