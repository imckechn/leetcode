import re

class Solution:
    def doMath(a, b, operator, multiplier):
        a = int(a)
        b = int(b)

        if operator == "+":
            if multiplier == "-":
                return a - b
            return a + b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return int(a/b)
        elif operator == "-":
            if multiplier == "-":
                return a + b
            return a - b
        else:
            print("number for operator")
            exit()

    def bedmass(expression, multiplier):
        first = ["/", "*"]
        second = ["+", "-"]

        i = 1
        while i < len(expression):
            if expression[i] in first:
                val = Solution.doMath(expression[i-1], expression[i+1], expression[i], "+")
                expression = expression[:i-1] + [val] + expression[i+2:]
            else:
                i = i+1

        i = 1
        while i < len(expression):
            if expression[i] in second:
                val = Solution.doMath(expression[i-1], expression[i+1], expression[i], multiplier)
                expression = expression[:i-1] + [val] + expression[i+2:]
            else:
                i = i+1
    
        return expression
    
    def findFirstOccurance(arr, char):
        for i in range(len(arr)):
            if arr[i] == char:
                return i
            
        return -1
    
    def findLastOccurance(arr, char):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == char:
                return i
            
        return -1
    
    def setNegativeNumbers(expression):
        if expression[0] == "-" and expression[1].isdigit():
            expression.pop(0)
            expression[0] = str(int(expression[0]) * -1)

        i = 1
        while i < len(expression)-1:
            if expression[i] == "-" and expression[i-1] == "(" and re.match(r"^-?(0|[1-9]\d*)(\.\d+)?$", expression[i+1]):
                expression[i+1] = str(int(expression[i+1]) * -1)
                expression.pop(i+2)
                expression.pop(i-1)
                expression.pop(i-1)
                i = i - 2
            else:
                i = i + 1

        return expression
    
    def distributeNeg(expression, multi):        
        for i in range(len(expression) - 1):
            if expression[i] == "-" and expression[i+1] == "(":
                nextBracket = Solution.findLastOccurance(expression[i:], ")")

                expression[i] = "+"
                if multi == "-":
                    expression = expression[:i] + Solution.distributeNeg(expression[i+1:nextBracket], "+") + expression[nextBracket:]
                else:
                    expression = expression[:i] + Solution.distributeNeg(expression[i+1:nextBracket], "-") + expression[nextBracket:]

                i = nextBracket

            elif expression[i] == "+" and multi == "-":
                expression[i] = "-"
            elif expression[i] == "-" and multi == "-":
                expression[i] = "+"
            elif expression[i] == "(":
                i = Solution.findLastOccurance(expression, ")")

        return expression

    def calculate(expression):
        expression = expression.replace(" ", "")
        expression = re.findall(r'\d+|[()+\-*/]', expression)
        expression = Solution.setNegativeNumbers(expression)
        expression = Solution.distributeNeg(expression, "+")

        if expression[0] == "+":
            expression.pop(0)
        
        openBracketIndex = Solution.findLastOccurance(expression, "(")
        while openBracketIndex != -1:
            multiplier = "+"
            closedBracketIndex = Solution.findFirstOccurance(expression[openBracketIndex:], ")") + openBracketIndex

            if expression[openBracketIndex - 1] == "-":

                if expression[0] == "-":
                    expression.pop(0)
                    openBracketIndex = openBracketIndex - 1
                    closedBracketIndex = closedBracketIndex - 1
                else:
                    expression[openBracketIndex - 1] = "+"


                multiplier = "-"
            soln = Solution.bedmass(expression[openBracketIndex+1:closedBracketIndex], multiplier)
            expression = expression[:openBracketIndex] + soln + expression[closedBracketIndex+1:]
            openBracketIndex = Solution.findLastOccurance(expression, "(")

        return int(Solution.bedmass(expression, "+")[0])
    
# print(Solution.calculate("1 + 2 ")) 
# print(Solution.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(Solution.calculate(" 2-1 + 2 "))
# print(Solution.calculate("0"))
# print(Solution.calculate("1-(     -2)"))
# print(Solution.calculate("1-(-(-(-2)))"))
# print(Solution.calculate("-(2 + 3)"))
# print(Solution.calculate("-2 + 3"))
print(Solution.calculate("- (3 + (4 + 5))"))