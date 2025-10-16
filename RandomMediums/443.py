from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        currentChar = chars[0]
        count = 1
        initialIndex = 0
        i = 1
        while i < len(chars):
            if chars[i] == currentChar:
                count += 1

            else:
                chars = chars[:initialIndex + 1] + chars[i:]                
                
                if count > 1:
                    countAsString = str(count)
                    for j, letter in enumerate(countAsString):
                        chars.insert(initialIndex + 1 + j, letter)

                    i = i - (count) + len(str(count)) + 1
                else:
                    i =  i - (count) + 1
                initialIndex = i
                currentChar = chars[i]
                count = 1
            i += 1

        chars = chars[:initialIndex + 1] + chars[i:]                       
        if count > 1:
            countAsString = str(count) 
            for j, letter in enumerate(countAsString):
                chars.insert(initialIndex + 1 + j, letter)
        return len(chars)


#Test 1
input = ["a","a","b","b","c","c","c"]
expected = ["a","2","b","2","c","3"]
answer = Solution.compress(None, input)
if (answer == expected):
    print("Q1: Passed")
else:
    print("Q1: Failed, should be -" + str(expected) + "- but got -" + str(answer) + "-")
    


#Test 2
input = ["a"]
expected = ["a"]
answer = Solution.compress(None, input)
if (answer == expected):
    print("Q2: Passed")
else:
    print("Q2: Failed, should be -" + str(expected) + "- but got -" + str(answer) + "-")
    


#Test 3
input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
expected = ["a","b","1","2"]
answer = Solution.compress(None, input)
if (answer == expected):
    print("Q3: Passed")
else:
    print("Q3: Failed, should be -" + str(expected) + "- but got -" + str(answer) + "-")
    

