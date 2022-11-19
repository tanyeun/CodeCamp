
class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                check = stack[-1]
                if check == "(" and char == ")" or \
                   check == "[" and char == "]" or \
                   check == "{" and char == "}":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0