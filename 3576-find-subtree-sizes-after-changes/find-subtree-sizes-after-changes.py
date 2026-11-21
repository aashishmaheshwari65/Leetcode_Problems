
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]
        last = [-1] * 26

        stack = [(0, True, -1)]

        while stack:
            node, entering, prev = stack.pop()
            c = ord(s[node]) - ord('a')

            if entering:
                prev = last[c]

                # Find closest ancestor with same character
                if prev != -1:
                    new_parent = prev
                else:
                    new_parent = parent[node]

                if node != 0:
                    new_children[new_parent].append(node)

                last[c] = node

                # Exit event restores ancestor state
                stack.append((node, False, prev))

                # Visit original children
                for child in reversed(children[node]):
                    stack.append((child, True, -1))

            else:
                last[c] = prev

        # Calculate subtree sizes in final tree
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        ans = [1] * n

        for node in reversed(order):
            for child in new_children[node]:
                ans[node] += ans[child]

        return ans
