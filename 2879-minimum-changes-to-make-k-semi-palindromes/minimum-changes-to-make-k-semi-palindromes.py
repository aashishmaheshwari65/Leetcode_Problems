
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute cost for every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    groups = length // d
                    changes = 0

                    for r in range(d):
                        for p in range(groups // 2):
                            left = i + r + p * d
                            right = i + r + (groups - 1 - p) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # DP
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):
                for j in range(2 * (t - 1), i - 1):
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
