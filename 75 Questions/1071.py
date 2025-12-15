class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest = min(len(str1), len(str2))
        longest = max(len(str1), len(str2))

        found = ""
        for i in range(1, shortest+1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                isMatch = True
                wordBeingChecked = str1[:i]
                for j in range(0, longest, i):
                    if len(str1) >= i+j and str1[j:i+j] != wordBeingChecked:
                        isMatch = False
                        break
                    if len(str2) >= i+j and str2[j:i+j] != wordBeingChecked:
                        isMatch = False
                        break

                if isMatch:
                    found = wordBeingChecked
        return found

sol = Solution()

# Test 0
inputA = "ABCABC"
inputB = "ABC"
expected = "ABC"

answer = sol.gcdOfStrings(inputA, inputB)
if answer != expected:
    print("Failed, got " + answer + ", expected " + expected)
else:
    print("Passed")
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