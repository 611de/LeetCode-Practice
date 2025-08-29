#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
               
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            if word[k]!=board[i][j]:
                return False
            if k == len(word)-1:
                return True
            board[i][j]=''
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0<=x<m and 0<=y<n and dfs(x, y, k+1):
                    return True
            board[i][j] = word[k]
            return False
        return any(dfs(i,j, 0) for i in range(m) for j in range(n)) 
# @lc code=end

