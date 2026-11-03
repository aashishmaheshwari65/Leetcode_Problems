class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(max(nums) - x for x in nums)