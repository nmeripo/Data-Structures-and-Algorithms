# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import * 
ListNode.__lt__ = lambda self, n2: self.val < n2.val

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Time Complexity : O (n * log k)
        heads = [head for head in lists if head]
        heapify(heads)
        result = None
        cur_node = None
        
        while heads:
            min_node = heappop(heads)
            
            if not result:
                result = cur_node = ListNode(min_node.val)
            else:
                cur_node.next = ListNode(min_node.val)
                cur_node = cur_node.next
                
            if min_node.next:
                heappush(heads, min_node.next)
                
        return result
            
        
        
