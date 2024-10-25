import re

class Solution:
    def calculate(expression):
        stack = []
        total = 0
        operator = 1
        currentNumber = 0

        for i in range(len(expression)):
            e = expression[i]

            if e.isdigit():
                currentNumber = currentNumber * 10 + int(e)

            else:
                total += int(currentNumber) * operator
                currentNumber = 0

                if e == "+" or e == "-":
                    if e == "-":
                        operator = -1
                    else:
                        operator = 1
                
                elif e == "(":
                    stack.append([total, operator])
                    total = 0
                    operator = 1

                elif e == ")":
                    combo = stack.pop(-1)
                    oldTotal = combo[0]
                    oldOperator = combo[1]

                    oldTotal += total * oldOperator
                    total = oldTotal

        total += int(currentNumber) * operator
        return total



    
print(Solution.calculate("1 + 2 ")) 
print(Solution.calculate("(1+(4+5+2)-3)+(6+8)"))
print(Solution.calculate(" 2-1 + 2 "))
print(Solution.calculate("0"))
print(Solution.calculate("1-(     -2)"))
print(Solution.calculate("1-(-(-(-2)))"))
print(Solution.calculate("-(2 + 3)"))
print(Solution.calculate("-2 + 3"))
print(Solution.calculate("- (3 + (4 + 5))"))
print(Solution.calculate("1-(5)"))
print(Solution.calculate("2-(5-6)"))
print(Solution.calculate("2-1-0+2+4+5-1"))
print(Solution.calculate("2108923"))