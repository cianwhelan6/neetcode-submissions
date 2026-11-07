class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        out = -1
        if target not in nums:
            return out
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] <= target:
                i = mid + 1
                out = mid
            else:
                j = mid - 1
        return out