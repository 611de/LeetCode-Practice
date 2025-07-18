#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def mid_order(p):
            if not p:
                return
            mid_order(p.left)
            self.count+=1
            if self.count==k:
                self.res = p.val
                return
            mid_order(p.right)
        mid_order(root)
        return self.res 
# @lc code=end

