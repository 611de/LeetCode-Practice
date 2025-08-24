#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(val=-10**5, next=None)
        # cur = head
        # while cur:
        #     sorted_list_cur = dummy
        #     while sorted_list_cur.next and sorted_list_cur.next.val<cur.val:
        #         sorted_list_cur = sorted_list_cur.next

        #     nxt = sorted_list_cur.next
        #     sorted_list_cur.next = cur
        #     next_cur = cur.next
        #     cur.next = nxt
        #     cur = next_cur
        # return dummy.next
        if not head or not head.next:
            return head
        left=right=head
        pre = head
        while right and right.next:
            right = right.next.next
            pre = left
            left = left.next
        
        pre.next = None
        def merge(list1, list2):
            dummy = ListNode()
            cur = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 if list1 else list2
            return dummy.next      
        head = self.sortList(head)
        left = self.sortList(left)
        head = merge(head, left)
        return head
        
        

        
        
# @lc code=end

