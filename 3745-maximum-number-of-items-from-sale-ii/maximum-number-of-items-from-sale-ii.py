class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        free = [0] * (n + 1)

        for f in range(1, n + 1):
            count = 0
            for j in range(f, n + 1, f):
                count += freq[j]

            free[f] = count - 1

        min_price = min(price for factor, price in items)
        bonus = []

        for factor, price in items:
            if price <= 2 * min_price and free[factor] > 0:
                bonus.append((price, free[factor]))

        bonus.sort()
        prefix_count = []
        prefix_cost = []
        count = 0
        cost = 0

        for price, capacity in bonus:
            count += capacity
            cost += price * capacity
            prefix_count.append(count)
            prefix_cost.append(cost)

        total_bonus = count
        def min_cost(target):
            q = min(target // 2, total_bonus)

            if q == 0:
                return target * min_price
            idx = bisect_left(prefix_count, q)

            previous_count = prefix_count[idx - 1] if idx > 0 else 0
            previous_cost = prefix_cost[idx - 1] if idx > 0 else 0
            bonus_cost = (
                previous_cost +
                (q - previous_count) * bonus[idx][0]
            )
            remaining = target - 2 * q
            return bonus_cost + remaining * min_price

        low = 0
        high = 2 * (budget // min_price) + 1
        while low + 1 < high:
            mid = (low + high) // 2

            if min_cost(mid) <= budget:
                low = mid
            else:
                high = mid
        return low