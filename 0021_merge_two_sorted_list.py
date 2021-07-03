# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 or l2:
            l = []
            while (l1 or l2):
                if l1 and l2:
                    v1 = l1.val
                    v2 = l2.val
                    if v2 > v1:
                        l.append(l1.val)
                        l.append(l2.val)
                    else:
                        l.append(l2.val)
                        l.append(l1.val)

                    l1 = l1.next
                    l2 = l2.next

                elif l1 and not l2:
                    l.append(l1.val)
                    l1 = l1.next

                else:
                    l.append(l2.val)
                    l2 = l2.next

            l = sorted(l)
            ln = ListNode(l[0])
            temp = ln
            for i in l[1:]:
                temp.next = ListNode(i)
                temp = temp.next
            return ln

        else:
            return None

# recursion way
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    elif not l2:
        return l1
    else:
        if l2.val > l1.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
