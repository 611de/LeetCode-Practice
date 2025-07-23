#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        
        def copy_list(head):
            if head==None:
                return None
            
            if not node_map.get(head):
                new_node = Node(head.val)
                node_map[head] = new_node
                new_node.next = copy_list(head.next)
                new_node.random = copy_list(head.random)
        return node_map[head]
# @lc code=end

