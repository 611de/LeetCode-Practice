#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry  = 0
        dummy = ListNode()
        cur = dummy
        while carry or l1 or l2:
            if l1:
                carry = carry + l1.val
                l1= l1.next
            if l2:
                carry = carry + l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry = carry//10
            cur = cur.next
        return dummy.next 
# @lc code=end

