#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_val+r_val+node.val)
            return max(max(l_val, r_val, 0) + node.val, 0)
        dfs(root)
        return ans

# @lc code=end

