#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(right, left):
            if not right and not left:
                return True
            if not right or not left:
                return False
            return (
                right.val == left.val
                and check(right.right, left.left)
                and check(right.left, left.right)
            )

        return check(root.right, root.left)


# @lc code=end
