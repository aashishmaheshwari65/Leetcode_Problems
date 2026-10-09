class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                if right_needed % 2 != 0:
                    insertions += 1  
                    right_needed -= 1 
                right_needed += 2
            else:
           
                if right_needed > 0:
                    right_needed -= 1
                else:
                    insertions += 1  
                    right_needed = 1 
                    
        return insertions + right_needed
