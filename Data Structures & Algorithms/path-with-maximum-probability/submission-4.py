class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[None] * n for _ in range(n)]

        # Build graph
        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            graph[a][b] = prob
            graph[b][a] = prob

        dist = [0.0] * n
        dist[start_node] = 1.0

        pq = [(-1.0, start_node)] # max heap

        while pq:
            neg_prob, u = heapq.heappop(pq)
            prob = -neg_prob

            if prob > dist[u]:
                continue

            if u == end_node:
                return prob

            for v in range(n):
                if graph[u][v] == None:
                    continue
                
                temp = prob * graph[u][v]

                if temp > dist[v]:
                    dist[v] = temp
                    heapq.heappush(pq, (-dist[v], v))
        
        return 0.0

                
