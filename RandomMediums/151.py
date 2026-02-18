class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s.reverse()

        i = 0
        while (i < len(s)):
            if s[i] == "":
                s.pop(i)
            else:
                s[i] += " "
                i+=1

        s = "".join(s)
        s = s[:len(s)-1]
        return s
    

sol = Solution()
# print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("  hello world  "))