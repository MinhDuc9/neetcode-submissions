class TreeNode:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar: 
    def __init__(self):
        self.tree = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.tree == None:
            self.tree = TreeNode(startTime, endTime)
            return True
        
        return self._insert(self.tree, startTime, endTime)

    def _insert(self, node: TreeNode, startTime: int, endTime: int) -> bool:
        if endTime <= node.start:
            if node.left == None:
                node.left = TreeNode(startTime, endTime)
                return True
            return self._insert(node.left, startTime, endTime)
        elif startTime >= node.end:
            if node.right == None:
                node.right = TreeNode(startTime, endTime)
                return True
            return self._insert(node.right, startTime, endTime)
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)