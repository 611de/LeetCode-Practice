#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        
        right_height = []
        left_height = []
        temp_max = 0
        for i in height:
            temp_max = max(i, temp_max) 
            right_height.append(temp_max)
        temp_max = 0
        for j in height[::-1]:
            temp_max = max(j, temp_max) 
            left_height.append(temp_max)
        left_height = left_height[::-1]
        res_height = [min(i, j) for i,j in zip(right_height, left_height)]
        return sum(res_height) - sum(height)
            



        
# @lc code=end

