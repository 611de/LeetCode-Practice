#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
       
        visited = [False] * len(rooms)

        def dfs(i):
            visited[i] = True
            for x in rooms[i]:
                if not visited[x]:
                    dfs(x)

        dfs(0)

        return all(visited)
 
# @lc code=end

