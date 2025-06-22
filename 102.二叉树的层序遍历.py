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
        stack=[root]
        res=[]
        while stack:
            current = stack.pop()
            res.append(current.val)
            if current.left:
                stack.append(current.left) 
            if current.right:
                stack.append(current.right) 
        return res
            

        
# @lc code=end

