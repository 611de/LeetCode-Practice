#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [0]*n

        def dfs(r, s):
            if r==n:
                res.append( ['.'*c+ 'Q'+'.'*(n-c-1) for c in col])
                return 
            for c in s:
                if all(R+col[R]!=r+c and R-col[R]!=r-c for R in range(r)):
                    col[r] = c
                    dfs(r+1, s-{c})
        dfs(0, set(range(n)))
        return res 
# @lc code=end

