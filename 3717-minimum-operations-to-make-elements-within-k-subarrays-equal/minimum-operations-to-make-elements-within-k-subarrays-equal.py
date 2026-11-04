
from typing import List
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        def update(bit, i, v):
            while i <= m:
                bit[i] += v
                i += i & -i

        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(bit, k):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and bit[nxt] < k:
                    idx = nxt
                    k -= bit[nxt]
                step >>= 1

            return idx + 1

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def add(v, delta):
            i = bisect_left(vals, v) + 1
            update(count, i, delta)
            update(sums, i, delta * v)

        # Calculate cost of the first window
        for v in nums[:x]:
            add(v, 1)

        def get_cost():
            mid_idx = kth(count, (x + 1) // 2)
            median = vals[mid_idx - 1]

            left_count = query(count, mid_idx - 1)
            left_sum = query(sums, mid_idx - 1)

            total_sum = query(sums, m)
            right_count = x - left_count - 1
            right_sum = total_sum - left_sum - median

            return (median * left_count - left_sum +
                    right_sum - median * right_count)

        costs = [get_cost()]

        # Sliding window costs
        for i in range(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)
            costs.append(get_cost())

        # Dynamic programming
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
