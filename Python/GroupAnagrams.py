class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) < 1:
            return []
        strs = sorted(strs)
        ana_table = {}
        for s in strs:
            sig = ''.join(sorted(s))
            if sig in ana_table:
                ana_table[sig].append(s)
            else:
                ana_table[sig] = [s]
        result = []
        for k,v in ana_table.items():
            result.append(v)
        return result
