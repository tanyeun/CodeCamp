import time
from typing import List
import matplotlib.pyplot as plt


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val


class DListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def construct_linked_list(ll: List):
    if len(ll) == 0:
        return None
    head = ListNode(ll[0])
    tmp = head
    for i in range(1, len(ll)):
        tmp.next = ListNode(ll[i])
        tmp = tmp.next
    return head


def construct_double_linked_list(ll: List):
    if len(ll) == 0:
        return None
    head = DListNode(ll[0])
    tmp = head
    for i in range(1, len(ll)):
        tmp.next = DListNode(ll[i])
        prev = tmp
        tmp = tmp.next
        tmp.prev = prev
    return head

def linked_list_identical(a: ListNode, b: ListNode):
    while a is not None and b is not None:
        if a.val != b.val:
            return False

        # If we reach here, then a and b
        # are not null and their data is
        # same, so move to next nodes
        # in both lists
        a = a.next
        b = b.next

    # If linked lists are identical,
    # then 'a' and 'b' must be null
    # at this point.
    return a is None and b is None


def double_linked_list_identical(a: ListNode, b: ListNode):
    while a is not None and b is not None:
        if a.val != b.val:
            return False
        if a.next is None:
            a_last = a
        if b.next is None:
            b_last = b
        a = a.next
        b = b.next
    a = a_last
    b = b_last
    while a is not None and b is not None:
        if a.val != b.val:
            return False
        a = a.prev
        b = b.prev
    return a is None and b is None


def pair_equal_non_order(pair1, pair2):
    if pair1[0] == pair2[0] and pair1[1] == pair2[1]:
        return True
    elif pair1[0] == pair2[1] and pair1[1] == pair2[0]:
        return True
    else:
        return False


def plot_2d_list(points):
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dx = points[i][0] - points[i][1]
            dy = points[i][1] - points[j][1]
            plt.plot(points[i][0], points[i][1], marker="o",
                     markersize=20, markeredgecolor="red",
                     markerfacecolor="green")
            plt.plot(points[j][0], points[j][1], marker="o",
                     markersize=20, markeredgecolor="red",
                     markerfacecolor="green")
            if dy == 0:
                plt.axline((points[i][0], points[i][1]),
                           (points[j][0], points[j][1]), color="#7FFF00")
            else:
                slope = dx / dy
                color = "blue"
                if -1 < slope <= 0:
                    color = "#E3CF57"
                if -2 < slope <= -1:
                    color = "#EE3B3B"
                if 0 < slope <= 1:
                    color = "#00FFFF"
                if 1 < slope <= 2:
                    color = "#76EEC6"
                if 2 < slope <= 3:
                    color = "#458B74"
                print(dx / dy, color)
                plt.axline((points[i][0], points[i][1]),
                           (points[j][0], points[j][1]), color=color)

    plt.show()

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f ns."
              % (func.__qualname__, time.time()*pow(10, 9) - start_time*pow(10, 9)))
        return result

    return measure_time
