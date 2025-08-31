#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i,c in enumerate(s)}
        res = []
        start = end = 0
        for i,c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                res.append(end-start+1)
                start = i+1
        return res 
# @lc code=end

