from typing import List, Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        possibleValues = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        digits = list(digits)
        answers = []

        for digit in digits:
            if len(answers) == 0:
                for char in possibleValues[digit]:
                    answers.append(char)
                continue

            else:
                ogLen = len(answers)
                answers = answers * len(possibleValues[digit])

                j = 0
                for char in possibleValues[digit]:
                    for i in range(ogLen):
                        answers[j + i] = answers[j + i] + char
                    j += i + 1

        answers.sort()
        return answers


            
print(Solution.letterCombinations(None, "23"))