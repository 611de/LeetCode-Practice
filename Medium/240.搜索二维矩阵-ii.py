#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i<m and j>=0:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                i+=1
            else:
                j-=1
        return False
# @lc code=end

