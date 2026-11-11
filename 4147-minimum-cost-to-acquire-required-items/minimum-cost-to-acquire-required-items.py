
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        # Option 1: Buy type 1 and type 2 separately
        option1 = (need1 * cost1) + (need2 * cost2)

        # Option 2: Buy type 3 items for both requirements
        option2 = max(need1, need2) * costBoth

        # Option 3: Buy type 3 for the common requirement,
        # then buy remaining items separately
        common = min(need1, need2)

        option3 = (
            common * costBoth
            + (need1 - common) * cost1
            + (need2 - common) * cost2
        )

        return min(option1, option2, option3)
