import re

class Solution:
    def doMath(a, b, operator):
        a = int(a)
        b = int(b)

        if operator == "+":
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return int(a/b)
        elif operator == "-":
            return a - b
        else:
            print("number for operator")
            exit()

    def evalRPN(tokens):
        i = 2
        while i < len(tokens):
            if not bool(re.match(r'^-?\d+$', tokens[i])):
                tokens[i-2] = Solution.doMath(tokens[i-2], tokens[i-1], tokens[i])
                tokens.pop(i)
                tokens.pop(i-1)
                i -= 1
            else:
                i += 1

        return int(tokens[0])

# print(Solution.evalRPN(["2","1","+","3","*"]))
print(Solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))