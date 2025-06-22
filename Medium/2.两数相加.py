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
            
        curor1 = l1
        curor2 = l2
        carry  = 0
        head = ListNode()
        new_list_cursor = head
        while True:
            if curor1 and curor2:
                new_value = curor1.val + curor2.val + carry 
                if new_value >= 10:
                    new_value = new_value - 10
                    carry  = 1
                else:
                    carry  = 0
                new_node = ListNode(new_value)
                new_list_cursor.next = new_node
                new_list_cursor = new_node
                curor1 = curor1.next
                curor2 = curor2.next
            if curor1 == None and curor2 == None:
                if carry  > 0:
                    new_node = ListNode(1)
                    new_list_cursor.next = new_node
                break 
            if curor1==None or curor2==None:
                if curor1:
                    new_value = curor1.val + carry 
                    curor1 = curor1.next
                if curor2:
                    new_value = curor2.val + carry 
                    curor2 = curor2.next

                if new_value >= 10:
                    new_value = new_value - 10
                    carry  = 1
                else:
                    carry  = 0

                new_node = ListNode(new_value)
                new_list_cursor.next = new_node
                new_list_cursor = new_node
        return head.next
            
# @lc code=end

