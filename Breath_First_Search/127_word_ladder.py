from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        adjacency = defaultdict(list)

        length = len(beginWord)
        for word in wordList:
            for i in range(len(word)):
                adjacency[word[:i] + "*" + word[i+1:]].append(word)

        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            current_word, level = queue.popleft()
            for i in range(length):
                intermediate_word = current_word[:i] + \
                    "*" + current_word[i + 1:]
                for word in adjacency[intermediate_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
            adjacency[intermediate_word] = []

        return 0
