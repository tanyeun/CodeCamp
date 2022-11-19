# leetcode 155
# 用兩個stack實現
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.min_stack) > 0 and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    # easy for inspection of stack
    def print(self):
        print(self.stack)
        print(self.min_stack)


if __name__ == "__main__":
    s = MinStack()
    s.print()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.print()
    print(s.getMin())
    s.print()
    print(s.pop())
    s.print()