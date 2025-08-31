#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(i, j):
            if i<0: return j+1
            if j<0: return i+1
            if word1[i]==word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j), dfs(i,j-1), dfs(i-1, j-1)) + 1
        return dfs(len(word1)-1, len(word2)-1) 
# @lc code=end

