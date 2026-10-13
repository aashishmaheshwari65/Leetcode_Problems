class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [x ** 2 for x in nums]
        
        squares.sort()
        
        neg_count = len(nums) // 2
        
        return sum(squares[neg_count:]) - sum(squares[:neg_count])
