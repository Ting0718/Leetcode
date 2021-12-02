'''two pointers'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

'''use visited list'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = []
        while head and head.next:
            if head in visited:
                return True
            else:
                visited.append(head)
                head = head.next
        return False


