class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * n
        inv_fact = [1] * n

        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)

        for i in range(n - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def comb(a, b):
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            return (
                comb(len(arr) - 1, len(left))
                * dfs(left) % MOD
                * dfs(right) % MOD
            )

        return (dfs(nums) - 1) % MOD