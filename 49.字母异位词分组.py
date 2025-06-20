#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_new = []
        for string in strs:
            chars = [i for i in string]
            chars.sort()
            new_string = "".join(chars)
            strs_new.append(new_string)
        res = {}
        for re_string, string in zip(strs_new, strs):
            if re_string in res:
                res[re_string].append(string)
            else:
                res[re_string] = [string]
        return list(res.values())


# @lc code=end
