#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_set = set()
        if not head or not head.next:
            return None
        cur = head
        while cur:
            if cur in node_set:
                return cur
            else:
                node_set.add(cur)
                cur = cur.next
        return None 
# @lc code=end

