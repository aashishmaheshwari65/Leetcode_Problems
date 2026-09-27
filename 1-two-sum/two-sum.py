class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in mp:
                return [mp[complement], i]

            mp[num] = i

        return []


        