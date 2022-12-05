class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    # easy for inspection of stack
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)

    s1 = Stack()
    input = "hello world, foo bar"
    for i in input:
        s1.push(i)

    reversed_input = ""
    while s1.is_empty() is False:
        reversed_input += s1.pop()

    print(reversed_input)