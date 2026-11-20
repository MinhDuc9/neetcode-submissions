class DisJoint:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.size[root_y] > self.size[root_x]:
            self.par[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.par[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        disJoint = DisJoint(n)
        accToGroup = {} # => store index of the account

        for i in range(n):
            m = len(accounts[i])
            for j in range(1, m):
                email = accounts[i][j]
                if email in accToGroup:
                    disJoint.union(i, accToGroup[email])
                else:
                    accToGroup[email] = i
        
        emailToGroup = collections.defaultdict(list)

        for k, v in accToGroup.items():
            rootGroup = disJoint.find(v)
            emailToGroup[rootGroup].append(k)
        
        res = []

        for k, v in emailToGroup.items():
            res.append( [accounts[k][0]] + sorted(v) )

        return res