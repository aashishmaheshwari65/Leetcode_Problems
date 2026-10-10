class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        k = k1 + k2
        
        if sum(diffs) <= k:
            return 0
            

        max_diff = max(diffs)
        buckets = [0] * (max_diff + 1)
        for d in diffs:
            buckets[d] += 1
            

        for d in range(max_diff, 0, -1):
            if buckets[d] == 0:
                continue
            

            take = min(k, buckets[d])
            buckets[d] -= take
            buckets[d - 1] += take
            k -= take
            
            if k == 0:
                break
                

        return sum(val * val * count for val, count in enumerate(buckets))
