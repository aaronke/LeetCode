    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.strip().split('.')
        v2 = version2.strip().split('.')
        neg = 1
        if len(v1) < len(v2):
            v1, v2 = v2, v1
            neg = -1
        for i in range(len(v1)):
            if i == len(v2):
                while i < len(v1):
                    if int(v1[i]) != 0:
                        return neg
                    i += 1
                return 0
            if int(v1[i]) > int(v2[i]):
                return neg
            if int(v1[i]) < int(v2[i]):
                return -1*neg
        return 0
