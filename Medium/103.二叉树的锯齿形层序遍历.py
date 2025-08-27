#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur = [root]
        res = []
        enev = False
        while cur:
            nxt = []
            vals = []
            for i in cur:
                vals.append(i.val)
                if i.left: nxt.append(i.left)
                if i.right: nxt.append(i.right)
            
            res.append(vals if not enev else vals[::-1])
            enev = not enev
            cur = nxt
        return res 
# @lc code=end

