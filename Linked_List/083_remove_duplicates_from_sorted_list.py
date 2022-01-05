class Solution(object):
    def deleteDuplicates(self, head):
        tmp = head
        while tmp:
            while tmp.next and tmp.next.val == tmp.val:
                tmp.next = tmp.next.next

            tmp = tmp.next

        return head
