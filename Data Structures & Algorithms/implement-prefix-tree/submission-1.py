class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]

        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            idx = ord(c) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        
        return True
        