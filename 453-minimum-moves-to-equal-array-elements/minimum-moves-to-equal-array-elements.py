class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = nums[0]
        total = 0

        for num in nums:
            total += num
            if num < min_num:
                min_num = num

        return total - min_num * len(nums)