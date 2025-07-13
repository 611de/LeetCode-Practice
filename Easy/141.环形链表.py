#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        faster = head.next
        while slow != faster:
            if not faster or not faster.next:
                return False
            slow = slow.next
            faster = faster.next.next
        return True
        
# @lc code=end

