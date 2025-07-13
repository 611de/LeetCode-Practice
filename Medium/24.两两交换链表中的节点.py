#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # method 1:
        # if not head or not head.next:
        #     return head
        # new_head = head.next
        # head.next = self.swapPairs(new_head.next)
        # new_head.next = head
        # return new_head
        # method 2:
        temp_node = ListNode(0, next=head)
        cur = temp_node
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            node2_next = node2.next

            node2.next = node1
            node1.next = node2_next
            cur.next = node2
            cur = node1
        return temp_node.next
# @lc code=end

