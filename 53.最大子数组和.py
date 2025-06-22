#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0
        for i in nums:
            cur_sum = i + cur_sum
            res = max(res, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return res


# @lc code=end
