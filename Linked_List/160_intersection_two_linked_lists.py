# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        tmpA = headA
        tmpB = headB

        while (tmpA != tmpB):
            if not tmpA:
                tmpA = headB
            else:
                tmpA = tmpA.next

            if not tmpB:
                tmpB = headA
            else:
                tmpB = tmpB.next

        return tmpA
