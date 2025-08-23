#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0=dummy
        n=0
        cur = head
        while cur:
            n+=1
            cur = cur.next

        cur = head
        pre = None        
        while n>=k:
            n-=k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            p0nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = p0nxt
        return dummy.next

# @lc code=end

