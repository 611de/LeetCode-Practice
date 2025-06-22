#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_res = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_res = max(max_res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_res


# @lc code=end
