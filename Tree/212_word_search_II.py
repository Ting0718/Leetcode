

'''Solution 2: Use Word Search Solution time limit exceeded'''
class Solution(object):
    def findWords(self, board, words):
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(r, c, i, word):
            if i == len(word):
                return word
            elif r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in path or board[r][c] != word[i]:
                return ""

            path.add((r, c))
            res = dfs(r + 1, c, i + 1, word) or dfs(r - 1, c, i + 1,
                                                    word) or dfs(r, c - 1, i + 1, word) or dfs(r, c + 1, i + 1, word)
            path.remove((r, c))
            return res

        res = []
        for word in words:
            for r in range(rows):
                for c in range(cols):
                    w = dfs(r, c, 0, word)
                    if w:
                        res.append(w)
            path = set()

        return list(set(res))
