#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = [""] * (2 * n)

        def dfs(left, right):
            if right == n:
                res.append(''.join(path))
                return
            if left < n:
                path[left + right] = "("
                dfs(left + 1, right)
            if right < left:
                path[left + right] = ")"
                dfs(left, right + 1)

        dfs(0, 0)
        return res

# @lc code=end

