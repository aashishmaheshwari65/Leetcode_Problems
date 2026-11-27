from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Calculate free copies received from buying each item type
        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        # dp[b] = maximum items obtainable with budget at most b
        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            bonus = free[i]

            old = dp[:]
            new = old[:]

            for b in range(price, budget + 1):
                # Buy the first copy of this item
                first = old[b - price] + bonus + 1

                # Buy another copy of this item
                extra = new[b - price] + 1

                new[b] = max(new[b], first, extra)

            dp = new

        return dp[budget]