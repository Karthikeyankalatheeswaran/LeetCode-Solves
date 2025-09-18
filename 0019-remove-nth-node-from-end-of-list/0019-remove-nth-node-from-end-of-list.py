# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        fast = dummy
        slow = dummy

#This loop is to skip the fast pointer ahead of 2 steps from slow pointer
        for i in range (n+1):
            fast = fast.next

#This loop traverses the ll
        while fast is not None:
            slow = slow.next
            fast = fast.next
#When the fast pointer is none or gone out of loop
        slow.next = slow.next.next
    #this deleted the n-th node

        return dummy.next
        