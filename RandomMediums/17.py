from typing import List


class Solution:
    buttonMap = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z'],
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return [""]
        
        combos = self.letterCombinations(digits[1:])
        letter = digits[:1]
        returnVal = []

        if int(letter) not in self.buttonMap.keys():
            return combos
        
        for elem in self.buttonMap[int(letter)]:
            returnVal += [elem+x for x in combos]

        return returnVal
    
sol = Solution()

#Test 1
digits = '23'
expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
answer = sol.letterCombinations(digits)

if answer == expected:
    print("Test 1 passed")
else:
    print("Test 1 failed")

#Test 2
digits = '2'
expected = ["a","b","c"]
answer = sol.letterCombinations(digits)

if answer == expected:
    print("Test 2 passed")
else:
    print("Test 2 failed")

    print("Test 1 failed")

#Test 3
digits = '210'
expected = ["a","b","c"]
answer = sol.letterCombinations(digits)

if answer == expected:
    print("Test 3 passed")
else:
    print("Test 3 failed")







