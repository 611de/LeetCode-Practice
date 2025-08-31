#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
def dfs(i, j):
    if i==0:
        return 0 if j==0 else inf

    if j<i*i:
        return dfs(i-1, j)
    return min(dfs(i-1, j), dfs(i, j-i*i)+1)

class Solution:
    
    def numSquares(self, n: int) -> int:
        
        return dfs(isqrt(n), n) 
# @lc code=end

