class Solution:
    def check(self, nums: List[int]) -> bool:
        m = (min(nums))
        i = nums.index(m)
        j = i
        check = []
        while i < len(nums):
            check.append(nums[i])
            i += 1
        i = 0
        while i < j:
            check.append(nums[i])
            i += 1
        print(check)
        if check == sorted(check):
            return True
        else:
            return False