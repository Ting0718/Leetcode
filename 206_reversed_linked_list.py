
''' get a reverse list and create a linked list through traversing the reverse list'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        l = []
        while head:
            l.append(head.val)
            head = head.next

        node = ListNode()
        tmp = node

        for i in range(len(l)-1, -1, -1):
            tmp.val = l[i]
            if i != 0:
                tmp.next = ListNode()
                tmp = tmp.next
        return node



''' recursively reverse the linked list'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head, newHead):
            if not head:
                return newHead

            next = head.next
            head.next = newHead
            newHead = head
            head = next

            return reverse(head, newHead)

        return reverse(head, None)
