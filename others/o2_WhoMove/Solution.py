
class Solution:
    @staticmethod
    def who_move(u, v):
        book = {}
        for i in range(len(u)):
            book[u[i]] = i

        offset = []
        for i in range(len(v)):
            offset.append(book[v[i]] - book[u[i]])

        odd = 0
        for i in range(len(offset)):
            if offset[i] not in [-1, 0, 1]:
                return i
            if offset[i] == 1:
                odd = i
        return odd