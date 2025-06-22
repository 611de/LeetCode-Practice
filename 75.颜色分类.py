#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i == 0:
                red += 1 
            elif i==1:
                white += 1
            else:
                blue += 1
        new_nums = red*[0] + white*[1] + blue*[2]
        for i in range(len(nums)):
            nums[i] = new_nums[i]
        
        
# @lc code=end

