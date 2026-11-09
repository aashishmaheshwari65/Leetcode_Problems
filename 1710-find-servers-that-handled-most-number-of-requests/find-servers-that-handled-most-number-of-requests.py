class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        count = [0] * k
        busy = []
        
        tree = [0] * (4 * k)

        def build(node, l, r):
            if l == r:
                tree[node] = 1
                return
            
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def update(node, l, r, idx, val):
            if l == r:
                tree[node] = val
                return
            
            mid = (l + r) // 2
            
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, l, r, ql, qr):
            if r < ql or l > qr or tree[node] == 0:
                return -1
            
            if l == r:
                return l
            
            mid = (l + r) // 2
            
            res = find(node * 2, l, mid, ql, qr)
            
            if res != -1:
                return res
            
            return find(node * 2 + 1, mid + 1, r, ql, qr)

        build(1, 0, k - 1)

        for i in range(len(arrival)):

            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(1, 0, k - 1, server, 1)

            start = i % k

            server = find(1, 0, k - 1, start, k - 1)

            if server == -1:
                server = find(1, 0, k - 1, 0, start - 1)

    
            if server == -1:
                continue

            count[server] += 1

            update(1, 0, k - 1, server, 0)

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
