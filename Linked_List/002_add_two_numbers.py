'''
reverse any iterable:
    iterable[::-1]
    
'''

# https://leetcode.com/problems/add-two-numbers
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''Better Solution: Use carry'''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = tail = ListNode()
        carry = 0

        # edge case when carry is not null
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0

            if l2:
                v2 = l2.val
            else:
                v2 = 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            tail.next = ListNode(val)

            # update pointers
            tail = tail.next
            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1 = ""
        num2 = ""
        while l1 or l2:
            while l1:
                num1 = str(l1.val) + num1
                l1 = l1.next

            while l2:
                num2 = str(l2.val) + num2
                l2 = l2.next

        s = str(int(num1) + int(num2))[::-1]
        print(s)
        dummy = tail = ListNode()
        for i in s:
            tail.next = ListNode(i)
            tail = tail.next

        return dummy.next
