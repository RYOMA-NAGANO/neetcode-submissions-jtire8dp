class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                operand.append(int(token))
            else:
                b = operand.pop()
                a = operand.pop()
                if token == "+":
                    operand.append(a + b)
                elif token == "-":
                    operand.append(a - b)
                elif token == "*":
                    operand.append(a * b)
                else:
                    operand.append(int(a / b))
        return operand[0]
