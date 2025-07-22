#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k%len(nums)
        def change_loc(nums, i, j):  
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        
        change_loc(nums, 0, len(nums)-1)
        change_loc(nums, 0, k-1)
        change_loc(nums, k, len(nums)-1)


# @lc code=end

