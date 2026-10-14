class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:

        if sum_val == 0 or sum_val > 9 * num:
            return ""
        
        count_of_9s = sum_val // 9
        remainder = sum_val % 9
        count_of_0s = num - count_of_9s - (1 if remainder > 0 else 0)
        

        result = "9" * count_of_9s
        if remainder > 0:
            result += str(remainder)
        result += "0" * count_of_0s
        
        return result
