class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        elif nums[-1] < nums[-2]:
            return nums[-1]
        left, right = 0, len(nums)-1
        while left<right-1:
            mid = (left+right)/2
            if nums[mid] < min(nums[mid+1], nums[mid-1]):
                return nums[mid]
            elif nums[mid] > max(nums[left], nums[right]):
                left = mid + 1
            elif nums[mid] < min(nums[left], nums[right]):
                right = mid - 1
            else:
                return nums[left]
        return min(nums[left],nums[right])
