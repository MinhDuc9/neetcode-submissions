class DisJoint:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] >= self.size[root_y]:
                self.par[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.par[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            
            self.num_components -= 1
            
            return True
        
        return False

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = DisJoint(n)
        
        for x, y in edges:
            uf.union(x, y)

        return uf.num_components