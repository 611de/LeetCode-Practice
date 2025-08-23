#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p1 = dummy
        while n>0:
            n-=1
            p1 = p1.next
        p2 = dummy
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return dummy.next 
# @lc code=end

