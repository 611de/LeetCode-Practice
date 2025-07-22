#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = [[0]*numCourses for i in range(numCourses)]
        indegree = [0]*numCourses
        for i,j in prerequisites:
            grid[i][j] = 1    
            indegree[j] +=1
        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.pop(0)
            count+=1
            for i in range(numCourses):
                if grid[node][i] == 1:
                    indegree[i]-=1             
                    if indegree[i]==0:
                        queue.append(i)
        return False if count<numCourses else True 
# @lc code=end

