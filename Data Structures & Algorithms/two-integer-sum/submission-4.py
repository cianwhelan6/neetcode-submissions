class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        out = []
        while i < len(nums) - 1:
            if target - nums[i] in nums[i+1:]:
               out.append(i) 
               j = i + 1
            i += 1
        while j < len(nums):
            if nums[j] == target - nums[out[0]]:
                out.append(j)
            j += 1
        return out