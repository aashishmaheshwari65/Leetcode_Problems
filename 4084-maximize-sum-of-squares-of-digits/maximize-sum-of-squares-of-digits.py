class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        # A positive integer cannot have a sum of 0, 
        # and the max possible sum for 'num' digits is 9 * num
        if sum_val == 0 or sum_val > 9 * num:
            return ""
        
        count_of_9s = sum_val // 9
        remainder = sum_val % 9
        count_of_0s = num - count_of_9s - (1 if remainder > 0 else 0)
        
        # Constructing the maximum possible integer
        result = "9" * count_of_9s
        if remainder > 0:
            result += str(remainder)
        result += "0" * count_of_0s
        
        return result
