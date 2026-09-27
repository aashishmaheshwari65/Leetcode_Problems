class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch == '(':
                stack.append([])
            
            elif ch == ')':
                current = stack.pop()
                current.reverse()

                if stack:
                    stack[-1].extend(current)
                else:
                    stack.append(current)
            
            else:
                if not stack:
                    stack.append([])

                stack[-1].append(ch)

        return ''.join(stack[0])

