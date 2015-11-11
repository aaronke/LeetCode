def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    if s is None or len(s) < 10:
        return []
    mapping = {}
    result = []
    for i in xrange(len(s)-9):
        if s[i:i+10] in mapping and mapping[s[i:i+10]]:
            result.append(s[i:i+10])
            mapping[s[i:i+10]] = False
        elif s[i:i+10] not in mapping:
            mapping[s[i:i+10]] = True
    return result
