# Moore counting magic, but last line list.count() is necessary
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if nums is None or len(nums) < 1:
        return []
    count1, candidate1, count2, candidate2 = 0, nums[0], 0, nums[0]
    for i in nums:
        if i == candidate1:
            count1 += 1
        elif i == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = i
            count1 += 1
        elif count2 == 0:
            candidate2 = i
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    return [n for n in set([candidate1, candidate2]) if nums.count(n) > len(nums)/3]
