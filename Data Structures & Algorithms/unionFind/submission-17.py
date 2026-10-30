class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        root = x
        while root != self.par[root]:
            root = self.par[root]

        while x != root:
            nxt = self.par[x]
            self.par[x] = root
            x = nxt
        
        return root

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.par[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.par[root_y] = root_x
            else:
                self.par[root_y] = root_x
                self.rank[root_x] += 1
            self.num_components -= 1
            return True
        
        return False

    def getNumComponents(self) -> int:
        return self.num_components
