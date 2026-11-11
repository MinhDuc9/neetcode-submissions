from typing import List

class Node:
    def __init__(self, total, L, R):
        self.total = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.root: Node = self.build(nums, 0, 0, len(nums) - 1)
    
    def build(self, nums: List[int], total: int, L: int, R: int) -> Node:
        if L == R:
            return Node(nums[L], L, R)
        
        M: int = (L + R) // 2
        root: Node = Node(total, L, R)
        root.left = self.build(nums, total, L, M)
        root.right = self.build(nums, total, M + 1, R)
        root.total = root.left.total + root.right.total
        

        return root

    def update(self, index: int, val: int) -> None:
        def dfs(node: Node, L: int, R: int) -> None:
            nonlocal val, index
            if L == R:
                node.total = val
                return
            
            M = (L + R) // 2

            if index <= M:
                dfs(node.left, L, M)
            else:
                dfs(node.right, M + 1, R)

            node.total = node.left.total + node.right.total
        
        dfs(self.root, 0, self.n - 1)

    def query(self, L: int, R: int) -> int:
        def queryRange(node: Node, L: int, R: int) -> int:
            if node.L == L and node.R == R:
                return node.total
            
            M = (node.L + node.R) // 2
            if L > M:
                return queryRange(node.right, L, R)
            elif R <= M:
                return queryRange(node.left, L, R)
            else:
                return queryRange(node.left, L, M) + queryRange(node.right, M + 1, R)
        
        return queryRange(self.root, L, R)


