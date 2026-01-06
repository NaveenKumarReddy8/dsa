from operator import add, floordiv, mul, sub, truediv


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+": add, "-": sub, "*": mul, "/": lambda a, b: int(a / b)}

        for char in tokens:
            if char in operators:
                operand_1, operand_2 = stack.pop(), stack.pop()
                stack.append(operators[char](operand_2, operand_1))
            else:
                stack.append(int(char))
        return stack[0]
