#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        a = 1
        b = 1
        for i in range(1, n):

            a, b = a + b, a

        return a


# @lc code=end
