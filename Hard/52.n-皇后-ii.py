#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        col = [0]*n

        def dfs(r, s):
            if r==n:
                res.append(1)
            for c in s:
                if all(r+c!=R+col[R] and r-c != R-col[R] for R in range(r)):
                    col[r] = c
                    dfs(r+1, s-{c})
        
        dfs(0, set(range(n)))

        return sum(res) 
# @lc code=end

