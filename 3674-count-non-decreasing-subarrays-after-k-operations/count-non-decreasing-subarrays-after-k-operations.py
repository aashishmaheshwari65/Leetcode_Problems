
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:

        dq = deque()
        n = len(nums)

        cost = 0
        ans = 0
        right = n - 1

        for left in range(n - 1, -1, -1):

            x = nums[left]
            count = 1

            # Update prefix maximums
            while dq and dq[0][0] < x:
                val, cnt = dq.popleft()
                cost += (x - val) * cnt
                count += cnt

            dq.appendleft([x, count])

            # Shrink window if cost exceeds k
            while cost > k:
                val, cnt = dq[-1]

                cost -= val - nums[right]
                cnt -= 1
                right -= 1

                if cnt == 0:
                    dq.pop()
                else:
                    dq[-1][1] = cnt

            ans += right - left + 1

        return ans
