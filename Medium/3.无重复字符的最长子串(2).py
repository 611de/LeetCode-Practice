#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        for right, x in enumerate(s):
            if x not in s[left:right]:
                res = max(res, right-left+1)
            else:
                while x in s[left:right]:
                    left+=1
        return res        
        
# @lc code=end

