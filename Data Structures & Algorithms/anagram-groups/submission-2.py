class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}

        out = []
        for word in strs:
            key = tuple(sorted(word)) # (a, c, t,) -> immutable
            if key not in dicts:
                dicts[key] = len(out)
                out.append([(word)])
            else:
                out[dicts[key]].append(word)
        return out