class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0] * (N+1)
        for c in citations:
            if c >= N:
                count[N] += 1
            else:
                count[c] += 1

        total = 0
        for i in range(N, -1, -1):
            total += count[i]
            if total >= i:
                return i