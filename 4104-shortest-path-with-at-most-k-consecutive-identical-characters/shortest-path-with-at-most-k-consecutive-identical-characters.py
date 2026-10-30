class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:

        if k < 1:
            return -1

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))


        start_char = labels[0]
        heap = [(0, 0, start_char, 1)]

        dist = {(0, start_char, 1): 0}

        while heap:
            cost, node, last_char, count = heapq.heappop(heap)

            state = (node, last_char, count)

            if cost != dist[state]:
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                char = labels[nxt]

                if char == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight
                new_state = (nxt, char, new_count)

                if new_cost < dist.get(new_state, float('inf')):
                    dist[new_state] = new_cost 
                    heapq.heappush(heap,(new_cost, nxt, char, new_count))

        return -1
