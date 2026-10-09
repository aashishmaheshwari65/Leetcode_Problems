class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        right_needed = 0
        
        for char in s:
            if char == '(':
                # If we needed an odd number of ')', it means we had a single ')' 
                # that needs to be closed before starting a new '(' group.
                if right_needed % 2 != 0:
                    insertions += 1  # Insert a ')'
                    right_needed -= 1 # We no longer need that single ')'
                right_needed += 2
            else:
                # We encountered a ')'
                if right_needed > 0:
                    right_needed -= 1
                else:
                    # No '(' is available to match this ')'. 
                    # We insert 1 '(' and now we need 1 more ')' to complete the '))' pair.
                    insertions += 1  
                    right_needed = 1 
                    
        # Any remaining right_needed must be added at the end
        return insertions + right_needed
