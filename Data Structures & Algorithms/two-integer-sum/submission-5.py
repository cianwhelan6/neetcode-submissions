class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        out = []
        while len(out) == 0:
            if target - nums[i] in nums[i+1:]:
               out.append(i) 
            i += 1
        while i < len(nums):
            if nums[i] == target - nums[out[0]]:
                out.append(i)
            i += 1
        return out