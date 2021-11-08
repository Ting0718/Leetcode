class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head
        for i in range(left - 1):
            # keep shifting prev and cur until cur gets to start reversed index
            leftPrev, cur = cur, cur.next
            # cur="left" leftPrev="node before left"

        # reverse from left to right
        prev = None
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        # connect to the entire linked list, update pointers
        leftPrev.next.next = cur  # cur is node after "right"
        leftPrev.next = prev  # prev is "right"

        return dummy.next
