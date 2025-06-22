#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in nums:
            if count==0:
                candidate=i
                count+=1
            else:
                if candidate==i:
                    count+=1
                else:
                    count-=1

        return candidate
         
# @lc code=end

