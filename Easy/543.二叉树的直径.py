#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def depth(p):
            if not p:
                return 0
            left = depth(p.left)
            right = depth(p.right)
            self.res = max(left + right, self.res)
            return max(left, right) + 1

        depth(root)
        return self.res


# @lc code=end
