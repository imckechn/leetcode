class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        word = strs[0]

        matchIndex = len(word)-1

        for i in range(1, len(strs)):
            if matchIndex == -1:
                return ""

            for j in range(matchIndex, -1, -1):
                if word[j] != strs[i][j]:
                    matchIndex = j-1

        return word[:matchIndex+1]

sol = Solution()
print(sol.longestCommonPrefix(["ab", "a"]))