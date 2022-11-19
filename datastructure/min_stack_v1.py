# 用一個stack實現
# 每一個stack value是tuple
# tuple的第二個值紀錄當前最小值
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = val

        if self.stack:
            minVal = min(minVal, self.stack[-1][1])

        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, minVal = self.stack[-1]
        return minVal

    def print(self) -> None:
        print(self.stack)


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