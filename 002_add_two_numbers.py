'''
reverse any iterable:
    iterable[::-1]
    
'''

# https://leetcode.com/problems/add-two-numbers
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    s1 = ""
    s2 = ""
    while l1 or l2:
        if l1:
            s1 += str(l1.val)
            l1 = l1.next
        if l2:
            s2 += str(l2.val)
            l2 = l2.next

    s1 = int(s1[::-1])
    s2 = int(s2[::-1])

    a = s1 + s2
    a = str(a)[::-1]

    l = ListNode(str(a)[0])
    temp = l

    for i in str(a)[1:]:
        temp.next = ListNode(int(i))
        temp = temp.next

    return l
