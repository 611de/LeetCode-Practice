#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                return res
            if i>0 and nums[i-1]==nums[i]:
                continue

            L = i+1
            R = len(nums)-1
            while L<R:
                if nums[i]+nums[L]+nums[R]==0:
                    res.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while L<R and nums[L]==nums[L-1]:
                        L+=1
                    while L<R and nums[R]==nums[R+1]:
                        R-=1
                elif nums[i]+nums[L]+nums[R]<0:
                    L+=1
                else:
                    R-=1
        return res
# @lc code=end

