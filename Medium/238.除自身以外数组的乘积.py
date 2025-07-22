#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        for i in nums:
            if not pre:
                pre.append(i)
            else:
                pre.append(pre[-1]*i)
        pre = [1] + pre[:-1]
        for i in nums[::-1]:
            if not suf:
                suf.append(i)
            else:
                suf.append(suf[-1]*i)
        suf = [1] + suf[:-1]
        suf = suf[::-1]
        res = []
        for i,j in zip(pre, suf):
            res.append(i*j)
        return res

# @lc code=end

