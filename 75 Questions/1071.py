class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest = min(len(str1), len(str2))
        longest = max(len(str1), len(str2))
        
        isMatch = False
        distance = shortest
        subString = ""
        if len(str1) == shortest:
            subString = str1
        else:
            subString = str2

        while not isMatch:
            isMatch = True

            if len(str1) % distance == 0 and len(str2) % distance == 0:
                for i in range(0, longest, distance):
                        if len(str1) >= i+distance and str1[i:i+distance] != subString:
                            isMatch = False
                            break
                        if len(str2) >= i+distance and str2[i:i+distance] != subString:
                            isMatch = False
                            break
            else:
                isMatch = False
            
            if not isMatch:
                distance = distance //2
                subString = subString[:distance]

            if subString == "":
                isMatch = True
        
        return subString

sol = Solution()

# Test 1
inputA = "TAUXXTAUXXTAUXXTAUXXTAUXX"
inputB = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
expected = "TAUXX"

answer = sol.gcdOfStrings(inputA, inputB)
if answer != expected:
    print("Failed, got " + answer + ", expected " + expected)
else:
    print("Passed")

#Test 2
inputA = "ABABAB"
inputB = "ABAB"
expected = "AB"

answer = sol.gcdOfStrings(inputA, inputB)
if answer != expected:
    print("Failed, got " + answer + ", expected " + expected)
else:
    print("Passed")

#Test 3
inputA = "LEET"
inputB = "CODE"
expected = ""

answer = sol.gcdOfStrings(inputA, inputB)
if answer != expected:
    print("Failed, got " + answer + ", expected " + expected)
else:
    print("Passed")

#Test 4
inputA = "AAAAAB"
inputB = "AAA"
expected = ""

answer = sol.gcdOfStrings(inputA, inputB)
if answer != expected:
    print("Failed, got " + answer + ", expected " + expected)
else:
    print("Passed")