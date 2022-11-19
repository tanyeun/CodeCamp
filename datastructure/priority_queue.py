import heapq
"""
优先队列常常用堆（heap）来实现。堆是一个完全二叉树，其每个节点的值总是大于等于子
节点的值

heapq is a binary heap, with O(log n) push and O(log n) pop
"""


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # get the root of the heap
    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)

    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

    print(pq)
