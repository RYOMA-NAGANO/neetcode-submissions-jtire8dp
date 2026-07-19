class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalDict = ["+", "-", "*", "/"]
        numStack = []
        for i in range(len(tokens)):
            if tokens[i] not in evalDict:
                numStack.append(int(tokens[i]))
            else:
                operand1 = numStack.pop()
                operand2 = numStack.pop()
                if tokens[i] == "+":
                    numStack.append(operand2 + operand1)
                elif tokens[i] == "-":
                    numStack.append(operand2 - operand1)
                elif tokens[i] == "*":
                    numStack.append(operand2 * operand1)
                else:
                    numStack.append(int(operand2 / operand1))
        return numStack[0]