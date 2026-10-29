class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        masks = [1 << (ord(c) - ord('a')) for c in s]

        
        parent = [-1] * n
        depth = [0] * n
        parent[0] = 0
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)


        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

    
        seg = [0] * (2 * n)

        for u in range(n):
            seg[n + pos[u]] = masks[u]

        for i in range(n - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(p, value):
            p += n
            seg[p] = value
            p //= 2

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p //= 2

        def range_xor(l, r):
    
            result = 0
            l += n
            r += n

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]

                l //= 2
                r //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        answers = []

        for query in queries:
            parts = query.split()
            u = int(parts[1])

            if parts[0] == "update":
                c = parts[2]
                masks[u] = 1 << (ord(c) - ord('a'))
                update(pos[u], masks[u])
            else:
                v = int(parts[2])
                mask = path_xor(u, v)

        
                answers.append((mask & (mask - 1)) == 0)

        return answers
