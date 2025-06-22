#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for i in nums[1:]:
            res = res^i
        return res
        
# @lc code=end

