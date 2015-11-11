# location the swap point, which is the first one from the end that drop down
def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if nums is None or len(nums) < 1:
        return
    partition = len(nums)-1
    while partition > 0:
        if nums[partition] > nums[partition-1]:
            break
        partition -= 1
    if partition > 0:
        swap_idx = len(nums)-1
        while swap_idx >= partition:
            if nums[swap_idx] > nums[partition-1]:
                break
            swap_idx -= 1
        nums[swap_idx], nums[partition-1] = nums[partition-1], nums[swap_idx]
    left, right = partition, len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
