class Node:
    def __init__(self, total: int, L: int, R: int):
        self.total = total
        self.L = L
        self.R = R
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.tree = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: List[int], L: int, R: int):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.total = root.left.total + root.right.total

        return root

    def update(self, index: int, val: int) -> None:
        def _update(node: Node):
            if node.L == node.R == index:
                node.total = val
                return
            
            M = (node.L + node.R) // 2
            if M < index:
                _update(node.right)
            else:
                _update(node.left)

            node.total = node.left.total + node.right.total

        _update(self.tree)

    def query(self, L: int, R: int) -> int:
        def query_search(node: Node, L: int, R: int) -> int:
            if node.L == L and node.R == R:
                return node.total
            
            M = (node.L + node.R) // 2
            if L > M:
                return query_search(node.right, L, R)
            elif R <= M:
                return query_search(node.left, L, R)
            else:
                return query_search(node.left, L, M) + query_search(node.right, M + 1, R)
        
        return query_search(self.tree, L, R)
