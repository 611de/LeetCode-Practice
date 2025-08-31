#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_right = 0
        next_right = 0
        for i in range(len(nums)-1):
            next_right = max(next_right, i+ nums[i])
            if cur_right==i:
                cur_right = next_right
                ans+=1
        return ans 
# @lc code=end

