class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # If opened > 0, it means this '(' is not the outermost one
                if opened > 0:
                    res.append(char)
                opened += 1
            else:  # char == ')'
                opened -= 1
                # If opened > 0 after decrementing, it means this ')' is not the outermost one
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)
