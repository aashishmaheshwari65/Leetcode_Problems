class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        E0 = [[0] * n for _ in range(m)]  
        E1 = [[0] * n for _ in range(m)]  
        S = [[0] * n for _ in range(m)]   

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    S[0][0] = 1
                    continue
                a = 0
                if j > 0:
                    a = S[i][j - 1]
                    if grid[i][j - 1] == 1:
                        a += E1[i][j - 1]
                b = 0
                if i > 0:
                    b = S[i - 1][j]
                    if grid[i - 1][j] == 1:
                        b += E0[i - 1][j]
                E0[i][j] = a % MOD
                E1[i][j] = b % MOD
                if grid[i][j] == 0:
                    S[i][j] = (E0[i][j] + E1[i][j]) % MOD

        return S[m - 1][n - 1] % MOD