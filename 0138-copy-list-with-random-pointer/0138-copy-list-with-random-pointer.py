"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        old_to_copy = {}

        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy_node = old_to_copy[curr]

            if curr.next:
                copy_node.next = old_to_copy[curr.next]
            
            if curr.random:
                copy_node.random = old_to_copy[curr.random]
                
            curr = curr.next
            
        return old_to_copy[head]

        