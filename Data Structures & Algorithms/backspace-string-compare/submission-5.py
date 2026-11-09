class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        st = []
        for i in s:
            if i != "#":
                ss.append(i)
            elif ss != []:
                ss.pop()
        for i in t:
            if i != "#":
                st.append(i)
            elif st != []:
                st.pop()
        if ss == st:
            return True
        else:
            return False