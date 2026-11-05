class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if i == "]" and len(stack) > 1:
                if stack[-2] == "[":
                    stack.pop()
                    stack.pop()
            elif i == ")" and len(stack) > 1:
                if stack[-2] == "(":
                    stack.pop()
                    stack.pop()
            elif i == "}" and len(stack) > 1:
                if stack[-2] == "{":
                    stack.pop()
                    stack.pop()
            elif i == "}" or i == "]" or i == ")":
                return False
        if stack == []:
            return True
        elif len(stack) > 0:
            return False