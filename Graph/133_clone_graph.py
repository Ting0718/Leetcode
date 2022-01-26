class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def clone(node):
            if node in oldToNew:  # already cloned
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                # append the copy to the neighbor
                copy.neighbors.append(clone(nei))

            return copy

        if not node:
            return None
        return clone(node)
