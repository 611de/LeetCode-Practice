#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        path = []
        res = []
        def dfs(i, start):
            if i==n:
                res.append(path.copy())
                return
            if i<n-1:
                dfs(i+1, start)
            
            t = s[start: i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(i+1, i+1)
                path.pop()
        dfs(0, 0)
        return res 
# @lc code=end

