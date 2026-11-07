class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)

        busy = []
        ans = []

        for j, task in enumerate(tasks):
            current_time = max(current_time if j > 0 else 0, j)

            # Release all servers available at current time
            while busy and busy[0][0] <= current_time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            # If no server is free, wait
            if not free:
                current_time = busy[0][0]

                while busy and busy[0][0] == current_time:
                    end, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            # Assign task
            w, i = heapq.heappop(free)
            ans.append(i)

            heapq.heappush(busy, (current_time + task, w, i))

        return ans