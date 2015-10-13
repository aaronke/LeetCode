class Solution(object):
    # just remove dups in the head and tail
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) < 1:
            return -1
        left, right = 0, len(nums)-1
        while left < right and nums[left] == nums[right]:
            left += 1
        while left <= right:
            mid = (left+right)/2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                if nums[mid] >= nums[left]:
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
                    if target < nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False        
