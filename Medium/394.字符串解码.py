#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp_str = ''
        res = ''
        mutil = 0
        for i in s:
            if i>= '0' and i<= '9':
                mutil = mutil*10 + int(i)
            elif i=='[':
                stack.append((mutil, temp_str))
                temp_str=''
                mutil=0
            elif i==']':
                mutil, res_str = stack.pop(-1)
                temp_str = res_str + mutil*temp_str
                mutil=0
            else:
                temp_str+=i
        return temp_str 
# @lc code=end

