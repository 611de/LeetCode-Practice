#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur = [root]
        res = []
        while cur:
            vals = []
            nxt = []
            for i in cur:
                vals.append(i.val)
                if i.left: nxt.append(i.left)
                if i.right: nxt.append(i.right)
            res.append(vals)
            cur = nxt
        return  res
         
# @lc code=end

