class Solution(object):
    # count freq and set
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 1:
            return
        zero_count, one_count = 0, 0
        for i in nums:
            if i == 0:
                zero_count += 1
            elif i == 1:
                one_count += 1
        idx = 0
        while zero_count > 0:
            nums[idx] = 0
            idx += 1
            zero_count -= 1
        while one_count > 0:
            nums[idx] = 1
            idx += 1
            one_count -= 1
        while idx < len(nums):
            nums[idx] = 2
            idx += 1
    # two pointer, one pass
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 1:
            return
        zero_idx, two_idx = 0, len(nums)-1
        i = 0
        while i <= two_idx:
            if nums[i] == 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
                i += 1 # increase i because the left part is granteed not have 2s
            elif nums[i] == 2:
                nums[i], nums[two_idx] = nums[two_idx], nums[i]
                two_idx -= 1                
            else:
                i += 1
            
