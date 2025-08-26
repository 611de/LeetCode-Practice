#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:    
        if k<=1:
            return 0
        prod = 1
        left = 0
        res = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod = prod/nums[left]
                left += 1
            res = res + right-left+1
        return res     
# @lc code=end

