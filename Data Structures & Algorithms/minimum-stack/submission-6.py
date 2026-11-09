class MinStack:

    def __init__(self):
        self.items = []
        self.d = {}
        self.min = None
        

    def push(self, val: int) -> None:
        self.items.append(val)
        if val in self.d:
            self.d[val] += 1
        else:
            self.d[val] = 1

    def pop(self) -> None:
        if self.d[self.items[-1]] == 1:
            self.d.pop(self.items[-1])
        else:
            self.d[self.items[-1]] -= 1
        return self.items.pop()
        
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return min(self.d)
        
