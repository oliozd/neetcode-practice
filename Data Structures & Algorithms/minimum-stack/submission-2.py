class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
    
    def pop(self) -> None:
        if self.stack: # If not empty
            top = self.stack.pop() # remove last pushed value and return into 'top'
            if self.minStack and self.minStack[-1] == top:
                self.minStack.pop()
            else:
                print("minStack empty")
        else:
            print("Stack empty")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            print("Stack empty")

    def getMin(self) -> int:
        if self.stack:
            minVal = float('inf')
            for i in self.stack:
                if i < minVal:
                    minVal = i
            return minVal
        else:
            print("Stack empty")

