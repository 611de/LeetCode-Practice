#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        left = 0
        ans = len(nums)+1
        for right, x in enumerate(nums):
            s = s + x
            while s-nums[left]>=target:
                s = s-nums[left]
                left+=1
            if s>=target:
                ans = min(ans, right-left+1)

        return ans if ans< len(nums)+1 else 0 
# @lc code=end

