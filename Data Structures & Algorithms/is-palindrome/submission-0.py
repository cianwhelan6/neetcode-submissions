class Solution:
    def isPalindrome(self, s: str) -> bool:
        inp = ""
        for l in s:
            if l.isalnum():
                inp += (l.lower())
        i = 0
        j = len(inp) - 1
        while i < len(inp) // 2:
            if inp[i] != inp[j]:
                return False
            i += 1
            j -= 1
        return True