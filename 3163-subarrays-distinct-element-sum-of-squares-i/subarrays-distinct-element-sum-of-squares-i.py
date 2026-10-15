class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        MOD = 10**9 + 7  
        
        for i in range(n):
            distinct_elements = set()
            for j in range(i, n):
                distinct_elements.add(nums[j])
                distinct_count = len(distinct_elements)
                total_sum += (distinct_count * distinct_count)
                
        return total_sum % MOD
