class Node:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: List[int], L: int, R: int):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        return self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return
        
        M = (root.L + root.R) // 2
        if index <= M:
            self.update_helper(root.left, index, val)
        else:
            self.update_helper(root.right, index, val)

        root.sum = root.left.sum + root.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)
    
    def query_helper(self, root, L, R):
        if L <= root.L and root.R <= R:
            return root.sum
        
        if R < root.L or L > root.R:
            return 0
        
        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)
