# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        
        import heapq

        min_heap = []
        
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next