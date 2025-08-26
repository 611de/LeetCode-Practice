#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt  = Counter(nums)
        max_cnt = max(cnt.values())

        buckets = [[] for _ in range(max_cnt+1)]

        for a,v in cnt.items():
            buckets[v].append(a)

        res = []
        for bucket in reversed(buckets):
            res = res + bucket
            if len(res)==k:
                return res
        
# @lc code=end

