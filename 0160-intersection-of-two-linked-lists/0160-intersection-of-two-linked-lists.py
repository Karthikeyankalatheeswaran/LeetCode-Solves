# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        ptr1 = headA
        ptr2 = headB

        while ptr1 is not ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA

        return ptr1

        #LOGIC ?
            # if ptr1 is None:
            #     ptr1 = headB
            # else:
            #     prt1 = ptr1.next

            # if ptr2 is None:
            #     ptr2 = headA
            # else:
            #     ptr2 = ptr2.next