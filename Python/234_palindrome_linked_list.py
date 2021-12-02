# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        fast = head
        slow = head

        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next

        secondHalfHead = self.reverse(slow.next)
        firstHalfHead = head

        while secondHalfHead and firstHalfHead:
            if firstHalfHead.val != secondHalfHead.val:
                return False

            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        return True

    def reverse(self, head: ListNode):
        newHead = None

        while head:
            next = head.next
            head.next = newHead
            newHead = head
            head = next

        return newHead
