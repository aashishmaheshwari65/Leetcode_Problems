class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left_remove = 0
        right_remove = 0

        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(i, balance, left_rem, right_rem, path):
 
            if balance < 0:
                return

            if left_rem < 0 or right_rem < 0:
                return

            if i == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.add("".join(path))
                return

            char = s[i]

            if char == '(':
                if left_rem > 0:
                    backtrack(
                        i + 1, balance, left_rem - 1,
                        right_rem, path
                    )

                path.append(char)
                backtrack(
                    i + 1, balance + 1,
                    left_rem, right_rem, path
                )
                path.pop()

            elif char == ')':
                if right_rem > 0:
                    backtrack(
                        i + 1, balance, left_rem,
                        right_rem - 1, path
                    )

                if balance > 0:
                    path.append(char)
                    backtrack(
                        i + 1, balance - 1,
                        left_rem, right_rem, path
                    )
                    path.pop()

            else:
                path.append(char)
                backtrack(
                    i + 1, balance,
                    left_rem, right_rem, path
                )
                path.pop()

        backtrack(0, 0, left_remove, right_remove, [])

        return list(result)