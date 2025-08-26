#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)
        res_left = -1
        res_right = len(s)
        left = 0
        for right, x in enumerate(s):
            cnt_s[x] +=1
            while cnt_s>=cnt_t:
                if res_right-res_left>right-left:
                    res_left, res_right = left, right
                cnt_s[s[left]]-=1
                left+=1
        return '' if res_left<0 else s[res_left: res_right+1]
             
# @lc code=end

