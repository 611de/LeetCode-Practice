#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def subTree(nums_sub):
            if len(nums_sub) == 0:
                return None

            mid = len(nums_sub) // 2
            left = subTree(nums_sub[:mid])
            right = subTree(nums_sub[mid + 1 :])
            root = TreeNode(nums_sub[mid], left, right)
            return root

        return subTree(nums)


# @lc code=end
