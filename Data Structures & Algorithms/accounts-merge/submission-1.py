class DisJoint:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x: int):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.size[root_x] >= self.size[root_y]:
                self.par[root_y] = root_x
                self.size[root_x] += self.size[root_y]
            else:
                self.par[root_x] = root_y
                self.size[root_y] += self.size[root_x]
        
        return None


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = DisJoint(n)
        emailToAcc = {} # email => index of acc

        for i, a in enumerate(accounts):
            m = len(a)
            for j in range(1, m):
                email = accounts[i][j]
                if email in emailToAcc:
                    uf.union(i, emailToAcc[email])
                else:
                    emailToAcc[email] = i

        emailToGroup = collections.defaultdict(list)
        for email, idx in emailToAcc.items():
            root = uf.find(idx)
            emailToGroup[root].append(email)

        res = []
        for root, email in emailToGroup.items():
            res.append( [accounts[root][0]] + sorted(email) )

        return res
