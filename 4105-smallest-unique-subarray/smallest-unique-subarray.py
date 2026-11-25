from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        nxt = [{}]
        link = [-1]
        length = [0]
        occ = [0]

        last = 0

        # Build suffix automaton
        for x in nums:
            cur = len(length)

            length.append(length[last] + 1)
            link.append(0)
            nxt.append({})
            occ.append(1)

            p = last

            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0

            else:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q

                else:
                    clone = len(length)

                    length.append(length[p] + 1)
                    link.append(link[q])
                    nxt.append(nxt[q].copy())
                    occ.append(0)

                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        # Counting sort states by their lengths
        size = len(length)
        count = [0] * (n + 1)

        for v in length:
            count[v] += 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]

        order = [0] * size

        for v in range(size - 1, -1, -1):
            l = length[v]
            count[l] -= 1
            order[count[l]] = v

        # Calculate occurrence counts
        for v in reversed(order):
            if v != 0:
                occ[link[v]] += occ[v]

        # Find minimum unique substring length
        ans = n

        for v in range(1, size):
            if occ[v] == 1:
                ans = min(ans, length[link[v]] + 1)

        return ans