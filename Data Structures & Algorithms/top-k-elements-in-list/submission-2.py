class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} 
        out = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        while k > 0:
            out.append(max(d, key = d.get))
            d.pop(max(d, key = d.get))
            k -= 1
        return out