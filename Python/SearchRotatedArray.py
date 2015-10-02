class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    if target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
        return -1
