"""
有問題，測試結果不太對
"""


class PriorityQueue:
    def __init__(self):
        self.elements = []

    # 获得最大值
    def top(self):
        return self.elements[0]

    # 插入任意值：把新的数字放在最后一位，然后上浮
    def put(self, k):
        self.elements.append(k)
        self._swim(len(self.elements)-1)

    # 删除最大值：把最后一个数字挪到开头，然后下沉
    def get(self):
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        self._sink(0)

    def _swim(self, pos):
        while pos > 1 and self.elements[pos//2] < self.elements[pos]:
            self.elements[pos//2], self.elements[pos] = self.elements[pos], self.elements[pos//2]
            pos /= 2

    def _sink(self, pos):
        N = len(self.elements)
        while 2 * pos <= N:
            i = 2 * pos
            if i < N and self.elements[i] < self.elements[i+1]:
                i += 1
            if self.elements[pos] >= self.elements[i]:
                break
            self.elements[pos], self.elements[i] = self.elements[i], self.elements[pos]
            pos = i

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    pq.put(3)
    pq.put(2)
    pq.put(4)
    pq.put(0)
    print(pq)
