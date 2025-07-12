#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        p = head
        while p:
            p_next = p.next
            p.next = pre
            pre = p
            p = p_next
        return pre
        # recursively method 
        # if head is None or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head
# @lc code=end

