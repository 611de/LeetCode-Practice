#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        brackets_map_re = {v:k for k,v in brackets_map.items()}
        stack = []
        for i in s:
            if i in brackets_map_re:
                if not stack or stack[-1]!=brackets_map_re[i]:
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(i)
        return not stack
        

        
# @lc code=end

