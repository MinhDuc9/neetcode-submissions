class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        

        for r in range(n):
            for c in range(m):
                value = board[r][c]
                if value == ".":
                    continue

                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[(r // 3, c // 3)]
                ):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)
        
        return True