

# go backwards and bubble up the sum to root, change data in place
class Solution:
    @staticmethod
    def rollup(tree, data):
        for i in range(len(tree)-1, 0, -1):
            parent = tree[i]
            data[parent] += data[i]
