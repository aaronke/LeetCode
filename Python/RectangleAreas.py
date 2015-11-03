class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        two_areas = (D-B)*(C-A) + (G-E)*(H-F)
        width = max(min(G,C) - max(A,E), 0)
        height = max(min(D,H) - max(B,F), 0)
        return two_areas - width*height
