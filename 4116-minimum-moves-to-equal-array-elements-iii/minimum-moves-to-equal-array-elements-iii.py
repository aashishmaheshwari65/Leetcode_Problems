class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)
        return sum(maximum - num for num in nums)