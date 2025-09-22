# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head #Edge Cases

        n = 1   #---------> To find the len of the list
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head #linking the tail to head , making it circular linked list

        rotate_steps = n - (k % n)  
        new_tail = head
        for _ in range(rotate_steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
        
