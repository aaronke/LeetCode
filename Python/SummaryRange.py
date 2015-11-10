    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums is None or len(nums) < 1:
            return []
        start, end = 0, 1
        result = []
        while end < len(nums):
            if nums[end-1] + 1 != nums[end]:
                if start == end - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start])+'->'+str(nums[end-1]))
                start = end
            end += 1
        if start == end - 1:
            result.append(str(nums[start]))
        else:
            result.append(str(nums[start])+'->'+str(nums[end-1]))
        return result
