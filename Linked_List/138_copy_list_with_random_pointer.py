class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # O(N), linear time
        # two loops: create deep copies and hashmap, pointer connecting
        oldToCopy = {None: None}
        tmp = head
        while tmp:
            copy = Node(tmp.val)
            oldToCopy[tmp] = copy
            tmp = tmp.next

        tmp = head
        while tmp:
            copy = oldToCopy[tmp]
            copy.next = oldToCopy[tmp.next]
            copy.random = oldToCopy[tmp.random]
            tmp = tmp.next

        return oldToCopy[head]
