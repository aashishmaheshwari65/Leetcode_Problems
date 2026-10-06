class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        total = 0

        for char in s:

            if char == '(':
                count = count + 1
            
            else:
                
                if count > 0:
                    count = count - 1 
                
                else:
                    total = total + 1

        return count + total


