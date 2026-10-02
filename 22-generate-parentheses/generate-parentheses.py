class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def dfs(current, left, right):

            if left == 0 and right == 0:
                result.append(current)
                return
            

            if left > 0:
                dfs(current + "(", left - 1, right)
                

            if right > left:
                dfs(current + ")", left, right - 1)

        dfs("", n, n)
        return result
