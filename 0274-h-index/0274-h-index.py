class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        result = sorted(citations)
        N = len(citations)
        hv = 0
        for i in range(N):
            hv = max(hv, min(result[i], N-i))
        return hv