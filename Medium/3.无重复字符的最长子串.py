#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            if len(s) > 0:
                return 1
            else:
                return 0
        max_len = 1
        for i in range(len(s)):

            sub_len = 1
            for j in range(i + 1, len(s)):
                if s[j] not in s[i:j]:
                    sub_len += 1
                    if max_len < sub_len:
                        max_len = sub_len
                else:
                    break

        return max_len


# @lc code=end
