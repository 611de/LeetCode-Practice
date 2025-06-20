#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_num = 0

        nums_set = set(nums)
        for i in nums_set:

            if i - 1 not in nums_set:
                now_num_len = 1
                j = i + 1
                while j in nums_set:
                    now_num_len += 1
                    j += 1
                longest_num = max(now_num_len, longest_num)
        return longest_num


# @lc code=end
