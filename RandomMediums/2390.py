class Solution:
    def removeStars(self, s: str) -> str:
        answer = []
        s = list(s)

        for char in s:
            if char == "*":
                answer.pop(-1)
            else:
                answer.append(char)

        return ''.join(answer)

#Test 1
if Solution.removeStars(None, "leet**cod*e") != "lecoe":
    print("Test 1: Failed")

else:
    print("Test 2: Passed")