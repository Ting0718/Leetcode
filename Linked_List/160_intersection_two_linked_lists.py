'''Solution 1: If reach the tail, point each head to other head'''
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

'''Solution 2: Hash Set'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        hashset_b = set()
        while headB:
            hashset_b.add(headB)
            headB = headB.next

        while headA:
            if headA in hashset_b:
                return headA
            headA = headA.next

        return headA
