#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_loc = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_loc.append(0)
        else:
            self.stack.append(val)
            if self.stack[self.min_loc[-1]] > val:
                self.min_loc.append(len(self.stack)-1)
            else:
                self.min_loc.append(self.min_loc[-1])

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_loc.pop(-1)        

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]        

    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[self.min_loc[-1]]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

