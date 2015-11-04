class Solution(object):
    # sort, and sequential scan, O(n*lgn)
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

class Solution(object):
    # hash count, O(n)
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) < 1:
            return 0
        count = [0]*(len(citations)+1)
        # count how many citations large than i index
        for c in citations:
            if c >= len(citations):
                count[-1] += 1
            else:
                count[c] += 1
        # accumulate the count
        for i in range(len(count)-2, -1, -1):
            count[i] += count[i+1]
        # find the first satisfied i index
        for i in range(len(count)-1, -1, -1):
            if count[i] >= i:
                return i
