# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseListIterative(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def reverseListRecursive(head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return prev
        cur = head.next
        head.next = prev
        return reverseListRecursive(cur, head)
            
            
            
        
        
