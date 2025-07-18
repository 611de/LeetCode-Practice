#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            next_queue = []
            right_val = 0
            while queue:
                node = queue.pop(0)
                right_val = node.val
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            res.append(right_val)
        return res


# @lc code=end
