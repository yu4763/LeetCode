class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0] * 1001
        for c in citations:
            count[c] += 1

        total = 0
        for i in range(1000, -1, -1):
            total += count[i]
            if total >= i:
                return i