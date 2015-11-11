def largestNumber(self, nums):
    nums = map(str,nums)
    nums.sort(cmp=lambda x, y: cmp(y+x, x+y))
    return ''.join(nums).lstrip('0') or '0'
