#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0]*(len(nums)+1)
        for i in range(len(nums)):
            s[i+1] = s[i] + nums[i]
        cnt = defaultdict(int)  
        res = 0
        for sj in s:
            res += cnt[sj-k]
            cnt[sj]+=1
        return res

        
# @lc code=end

