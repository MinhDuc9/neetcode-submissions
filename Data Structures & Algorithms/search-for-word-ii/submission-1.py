class PrefixTrie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        n = len(word)

        def dfs(cur, idx):
            if idx == n:
                cur.isWord = True
                return
            c = word[idx]
            if c not in cur.children:
                cur.children[c] = PrefixTrie()
            dfs(cur.children[c], idx + 1)
        
        dfs(self, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        treeSearch = PrefixTrie()

        for w in words:
            treeSearch.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()

        def dfs(r, c, node, word):
            if ((r < 0 or c < 0) or (r >= ROWS or c >= COLS) or 
                (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord == True:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, treeSearch, "")
        
        return list(res)
