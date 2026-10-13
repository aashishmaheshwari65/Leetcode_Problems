class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # If the string is empty or only had spaces
        if i == n:
            return 0
            
        # 2. Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Conversion: Read the integer digits
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i]) # Converting a single char digit is allowed
            
            # Check for overflow/underflow before multiplying
            if res > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            i += 1
            
        return sign * res
