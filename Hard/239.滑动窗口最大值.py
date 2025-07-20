#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_queue = []
        res = []
        for i in range(len(nums)):
            while max_queue and nums[max_queue[-1]]<nums[i]:
                max_queue.pop(-1)
            max_queue.append(i)

            left = i-k+1
            if max_queue[0]<left:
                max_queue.pop(0)
            
            if left>= 0:
                res.append(nums[max_queue[0]])
        return res

            

# @lc code=end

