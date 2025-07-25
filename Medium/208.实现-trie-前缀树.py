#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start

class Node():
    def __init__(self):
        self.end = False
        self.s = {}

class Trie:

    def __init__(self):
        self.root = Node()               

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not cur.s.get(i):
                cur.s[i] = Node()
            cur = cur.s[i]
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root
        for i in word:
            if not cur.s.get(i):
                return -1
            cur = cur.s[i]
        return 1 if cur.end else 0    

    def search(self, word: str) -> bool:
        if self.find(word)==1:
            return True        
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if self.find(prefix)>=0:
            return True
        else:
            return False       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

