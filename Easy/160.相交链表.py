#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None or headB==None:
            return None
        pa = headA
        pb = headB
        while pa!=None or pb!=None:
            if pa==pb:
                break
            if pa != None:
                pa = pa.next
            else:
                pa = headB
            if pb != None:
                pb = pb.next
            else:
                pb = headA
        return pa
                
# @lc code=end
