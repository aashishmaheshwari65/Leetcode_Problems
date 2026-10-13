class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Convert all elements to their squared values
        squares = [x ** 2 for x in nums]
        
        # Sort squares in ascending order
        squares.sort()
        
        # The first n // 2 elements are the smallest and should be subtracted
        # The remaining elements are the largest and should be added
        neg_count = len(nums) // 2
        
        return sum(squares[neg_count:]) - sum(squares[:neg_count])
