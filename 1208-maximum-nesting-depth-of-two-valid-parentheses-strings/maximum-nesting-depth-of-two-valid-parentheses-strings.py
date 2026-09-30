class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        depth = 0
        answer = []

        for i in seq:
            if i == '(':
                depth = depth+1
                answer.append(depth%2)
            else:
                answer.append(depth%2)
                depth = depth -1
        
        return answer