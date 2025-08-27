#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_dep = [0]*numCourses

        for l, r in prerequisites:
            graph[r].append(l)
            in_dep[l] +=1
        res = []
        queue = deque([i for i, d in enumerate(in_dep) if d==0])
        while queue:
            node  = queue.popleft()
            res.append(node)
            for x in graph[node]:
                in_dep[x]-=1
                if in_dep[x]==0:
                    queue.append(x)
        return res if len(res)==numCourses else [] 
# @lc code=end

