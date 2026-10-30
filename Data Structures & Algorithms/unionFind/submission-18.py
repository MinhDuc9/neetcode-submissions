class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [0] * n
        self.num_components = n

    def find(self, x: int) -> int:
        # Compression path code
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])

        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] < self.size[root_y]:
                self.par[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.par[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            self.num_components -= 1
            return True
        
        return False

    def getNumComponents(self) -> int:
        return self.num_components
