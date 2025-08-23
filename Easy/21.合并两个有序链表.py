#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode()
        head = dummy
        cur = head
        while p1 and p2:
            if p1.val< p2.val:
                cur.next = p1
                p1 = p1.next
                cur = cur.next
            else:
                cur.next = p2
                p2 = p2.next
                cur = cur.next
        if p1:
            cur.next = p1
        else:
            cur.next = p2
        return dummy.next
            
# @lc code=end

