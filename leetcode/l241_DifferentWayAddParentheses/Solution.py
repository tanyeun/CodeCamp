from typing import List


class Solution:
    @staticmethod
    def diff_ways_to_compute(expression: str) -> List[int]:
        if '+' not in expression and '-' not in expression \
                            and '*' not in expression:
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left, right = map(Solution.diff_ways_to_compute, (expression[:i], expression[i+1:]))
                for a in left:
                    for b in right:
                        res.append(eval('{}{}{}'.format(a, char, b)))
        return res
