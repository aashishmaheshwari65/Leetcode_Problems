from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        count = {}
        ans = [0] * len(queries)
        left = right = 0

        for t, idx in q:
            # Add logs within the right boundary
            while right < len(logs) and logs[right][1] <= t:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs before the left boundary
            while left < right and logs[left][1] < t - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans