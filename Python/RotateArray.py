class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        # reverse using two pointers
        left, right = 0, n-1
        self.reverse(nums, left, right)
        left, right = 0, k-1
        self.reverse(nums, left, right)
        left, right = k, n-1
        self.reverse(nums, left, right)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
#####################################################################
        # reverse using list
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]        
        
        # dup-cat array, space O(N)
        tmp = nums + nums
        nums[:] = tmp[n-k:n-k+n]
        
        # sub-array method, space O(N)
        tmp = nums[n-k:]+nums[:n-k]
        nums[:] = tmp[:]
