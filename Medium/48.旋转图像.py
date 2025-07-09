#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp_matrix=[]
        for i in range(len(matrix)):
            line = []
            for j in range(len(matrix)-1,0):
                line.append(matrix[j][i])
            temp_matrix.append(line)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = temp_matrix[i][j]

        
# @lc code=end

