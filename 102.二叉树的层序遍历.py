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
        stack1=[]
        stack2=[]
        res=[]
        res1=[]
        if root:
            stack1.append(root)

        while stack1:
            current = stack1.pop(0)
            res1.append(current.val)
           
           
            if current.left:
                stack2.append(current.left) 
            if current.right:
                stack2.append(current.right)
            if not stack1:
                stack1 = stack2
                stack2 = []
                res.append(res1)
                res1 = []
        return res
            

        
# @lc code=end

