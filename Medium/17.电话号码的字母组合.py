#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map1_9 = {'2': 'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        
        res = []
        path = []
        n = len(digits)
        if n==0:
            return []
        def dfs(i):
            if i==n:
                res.append(''.join(path.copy()))
            else:
                for x in map1_9[digits[i]]:
                    path.append(x)
                    dfs(i+1)
                    path.pop()
        dfs(0)
        return res
# @lc code=end

