#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for i in range(len(intervals)):
            if not merged:
                merged.append(intervals[i])
            elif merged[-1][1] >= intervals[i][0]:
                merged[-1] = [merged[-1][0], max(intervals[i][1], merged[-1][1])]
            else:
                merged.append(intervals[i])
        return merged
                

# @lc code=end

