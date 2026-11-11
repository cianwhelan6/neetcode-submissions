class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        while k > 0:
            g = max(gifts)
            i = gifts.index(g)
            gifts[i] = int(g ** (1/2))
            k -= 1 
        print(gifts)
        total = 0
        for i in gifts:
            total += i
        return total