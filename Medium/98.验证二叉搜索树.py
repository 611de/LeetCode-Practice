#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        stack=[]
        current = root
        while stack or current:
             
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        old_res = res.copy()
        res.sort()
        return old_res == res and len(set(res)) == len(res)
# @lc code=end

