#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res_row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    res_row.append(1)
                else:
                    res_row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(res_row)
        return res


# @lc code=end
