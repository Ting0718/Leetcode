class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # we could just record the result of each row and column instead of each mmove
        n = 3
        # plyaer win if the value of any line = n or = -n
        rows = [0] * n
        cols = [0] * n
        diag = anti_diag = 0
        player = 1
        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diag += player  # diag
            if row + col == n - 1:  # anti diag
                anti_diag += player

            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                if player == 1:
                    return "A"
                else:
                    return "B"

            player = player * -1

        if len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"

