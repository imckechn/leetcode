class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = ""
        lastIndex = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if lastIndex == i+1:
                    lastIndex = i
                    continue

                sentence += s[i+1:lastIndex] + " "
                lastIndex = i

        sentence += s[:lastIndex]

        while sentence[0] == " ":
            sentence = sentence[1:]
        
        while sentence[-1] == " ":
            sentence = sentence[:len(sentence)-1]

        return sentence

# # Test 1
# input = "the sky is blue"
# ans = "blue is sky the"
# ret = Solution.reverseWords(None, input)

# if ret == ans:
#     print("Q1: Passed")
# else:
#     print("Q1: Failed -" + ret + "-")


# Test 2
input = "  hello world  "
ans = "world hello"
ret = Solution.reverseWords(None, input)

if ret == ans:
    print("Q2: Passed")
else:
    print("Q2: Failed -" + ret + "-")


# Test 3
input = "a good   example"
ans = "example good a"
ret = Solution.reverseWords(None, input)

if ret == ans:
    print("Q3: Passed")
else:
    print("Q3: Failed -" + ret + "-")


# Test 3
input = " asdasd df f"
ans = "f df asdasd"
ret = Solution.reverseWords(None, input)

if ret == ans:
    print("Q3: Passed")
else:
    print("Q3: Failed -" + ret + "-")