#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(arr, k):     
            key = arr[0]
            small=[]
            equel=[]
            large=[]
            for i in arr:
                if i < key:
                    small.append(i)
                elif i==key:
                    equel.append(i)
                else:
                    large.append(i)

            if k<=len(large):
                return quick_select(large, k)
            elif k>len(large) and k<= len(large)+len(equel):
                return key
            else:
                return quick_select(small,  k - len(large) - len(equel))
        return quick_select(nums, k) 
# @lc code=end

