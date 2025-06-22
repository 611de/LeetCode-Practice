#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            j=i
            sum = nums[i]
            while sum < k:
                j += 1
                sum = nums[j] 
            if sum==k:
                count+=1
        return count
            

        
# @lc code=end

