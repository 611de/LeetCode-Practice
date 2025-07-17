#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_loc = -1
        second_loc = -1
        for i in range(len(nums)):
            if nums[i]==target:
                if first_loc==-1:
                    first_loc=i
                    second_loc=i
                else:
                    second_loc=i                
        return [first_loc, second_loc]
# @lc code=end

