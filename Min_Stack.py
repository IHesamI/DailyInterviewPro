class minStack(object):
    def __init__(self):
        # Fill this in.
        self.stack = []
        self.min = None

    def search_min(self):
        try:
            self.min = self.top()
            for x in self.stack:
                if x < self.min:
                    self.min = x
        except Exception:
            self.min = None

    def push(self, x):
        if self.min == None or self.min > x:
            self.min = x
        self.stack.append(x)

    def pop(self):
        if self.stack:
            popedvalue = self.stack.pop()
            if popedvalue == self.min:
                self.search_min()
            return popedvalue
        else:
            raise Exception

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise Exception

    def getMin(self):
        return self.min


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2
