# Solution 1: Use fast and slow pointer
class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Solution 2: use a counter
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next

        count = 0
        mid = (length // 2) + 1

        tmp = head
        while tmp:
            count += 1
            if count == mid:
                return tmp
            tmp = tmp.next
