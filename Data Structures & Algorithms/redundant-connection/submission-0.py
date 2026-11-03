class DisJoin:
    def __init__(self, n: int):
        self.par: Dict[int, int] = {}
        self.rank: Dict[int, int] = {}
        self.components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, x: int) -> int:
        if self.par[x] != x:
            return self.find(self.par[x])

        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.par[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.par[root_y] = root_x
            else:
                self.par[root_y] = root_x
                self.rank[root_x] += 1
            self.components -= 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = DisJoin(n)

        for x, y in edges:
            if graph.union(x - 1, y - 1) == False:
                return [x, y]

        return []