from typing import List

class Node:
    def __init__(self, total: int, L: int, R: int):
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        self.total = total
    
    def __str__(self) -> str:
        output = ""
        def print_tree(node: Node, L: int, R: int, level: int):
            nonlocal output
            M = (L + R) // 2
            if node.left:
                print_tree(node.left, L, M, level + 1)
            output += " " * level + str(node.total) + "\n"
            if node.right:
                print_tree(node.right, M + 1, R, level + 1)            
        
        print_tree(self, self.L, self.R, 0)
        return output

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.root = self.build(nums, 0, self.n - 1)
    
    def build(self, nums: List[int], L: int, R: int):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2
        root: Node = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.total = root.left.total + root.right.total
        
        return root
    
    def update(self, index: int, val: int) -> None:
        root = self.root

        def dfs(node: Node) -> None:
            if node.L == index and node.R == index:
                node.total = val
                return
            
            M = (node.L + node.R) // 2
            if M < index:
                dfs(node.right)
            else:
                dfs(node.left)
            
            node.total = node.left.total + node.right.total
        
        dfs(root)
    
    def query(self, L: int, R: int) -> int:
        root = self.root

        def searchRange(node: Node, Left: int, Right: int):
            if node.L == Left and node.R == Right:
                return node.total
            
            M = (node.L + node.R) // 2
            if Left > M:
                return searchRange(node.right, Left, Right)
            elif Right <= M:
                return searchRange(node.left, Left, Right)
            else:
                return searchRange(node.left, Left, M) + searchRange(node.right, M + 1, Right)

        return searchRange(root, L, R)
