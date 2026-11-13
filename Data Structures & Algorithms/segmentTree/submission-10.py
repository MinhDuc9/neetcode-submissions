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
        self.root = self.build(nums, 0, self.n - 1)

    def build(self, nums: List[int], L: int, R: int) -> Node:
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.total = root.left.total + root.right.total

        return root
    
    def update(self, index: int, val: int) -> None:
        def dfs(node: Node) -> None:
            if node.L == index and node.R == index:
                node.total = val
                return

            M = (node.L + node.R) // 2
            if index <= M:
                dfs(node.left)
            else:
                dfs(node.right)
            
            node.total = node.left.total + node.right.total
             
        
        node = self.root
        dfs(node)
    
    def query(self, L: int, R: int) -> int:
        node = self.root

        def searchQuery(node: Node, Left: int, Right: int) -> int:
            if node.L == Left and node.R == Right:
                return node.total
            
            M = (node.L + node.R) // 2

            if Left > M:
                return searchQuery(node.right, Left, Right)
            elif Right <= M:
                return searchQuery(node.left, Left, Right)
            else:
                return searchQuery(node.left, Left, M) + searchQuery(node.right, M + 1, Right)
        
        return searchQuery(node, L, R)
