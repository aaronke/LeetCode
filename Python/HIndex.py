class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) < 1:
            return 0
        citations = sorted(citations)
        n = len(citations)
        for h in range(n,0,-1):
            if citations[n-h] >= h and (n-h-1 < 0 or citations[n-h-1] <= h):
                return h
        return 0
