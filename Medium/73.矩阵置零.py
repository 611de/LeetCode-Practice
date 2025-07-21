#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = []
        zero_col = []
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == 0:
                    zero_row.append(i)
                    zero_col.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
# @lc code=end

