#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        chars = [i for i in p]
        chars.sort()
        p_reorder = ''.join(chars)
        for i in range(len(s) - len(p)+1):
            sub_str = s[i: i+len(p)]
            sub_str_char = [char for char in sub_str]
            sub_str_char.sort()
            sub_str_reorder = ''.join(sub_str_char)
            if sub_str_reorder == p_reorder:
                res.append(i)
        return res


        
# @lc code=end

