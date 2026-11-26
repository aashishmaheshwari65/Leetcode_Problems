class Solution:
    def canAliceWin(self, n: int) -> bool:
        def win(stones, remove):
            if stones < remove:
                return False
            return not win(stones - remove, remove - 1)

        if n < 10:
            return False

        return not win(n - 10, 9)