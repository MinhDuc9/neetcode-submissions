class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[None] * n for _ in range(n)]

        # Build graph
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a][b] = p
            graph[b][a] = p
        
        dist = [0.0] * n
        dist[start_node] = 1.0

        pq = [(-1.0, start_node)] # Prob, start node. MAX HEAP

        while pq:
            neg_prob, u = heapq.heappop(pq)
            cur_prob = -neg_prob

            if cur_prob > dist[u]:
                continue
            
            if u == end_node:
                return cur_prob

            for v in range(n):                
                if graph[u][v] != None:
                    p = dist[u] * graph[u][v]
                    if dist[v] < p:
                        dist[v] = p
                        heapq.heappush(pq, (-p, v))

        return 0.0
